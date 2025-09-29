from odoo import models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        company_id = self.env.company

        if self.sale_order_template_id.fee_calc:
            self._check_fee_cfg_fields(company_id)
            fee_product_id = company_id.fee_product_id

            fee_line_id = self.order_line.filtered(lambda ol: ol.product_id.id == fee_product_id.id)

            if not fee_line_id:
                raise ValidationError('La plantilla seleccionada debe tener calculado un Fee')

        return super().action_confirm()

    def btn_compute_fee(self):
        company_id = self.env.company
        self._check_fee_cfg_fields(company_id)

        fee_product_id = company_id.fee_product_id
        fee_percentage = self.partner_id.percentage_fee or company_id.def_percentage_fee

        fee_line_id = self.order_line.filtered(lambda ol: ol.product_id.id == fee_product_id.id)
        sol_ids = self.order_line - fee_line_id

        base_imponible = sum(sol_ids.mapped('price_subtotal'))
        fee_result = base_imponible * fee_percentage

        if fee_line_id:
            fee_line_id.price_unit = fee_result
        else:
            self.order_line = [(0,0, {'product_id': fee_product_id.id,
                                      'product_uom_qty': 1,
                                      'dias': 1,
                                      'precio_unitario_dias': fee_result,
                                      'price_unit': fee_result,
                                      'tax_id': False,
                                      'x_studio_costo': 1,
                                      })]

        self.order_line._compute_tax_id()
        for line in self.order_line:
            line._onchange_product_brighsolutions()
        self.onchange_margen_total()

    def _check_fee_cfg_fields(self, company_id):
        if not company_id.def_percentage_fee:
            raise ValidationError('Debe configurar el porcentaje por defecto del Fee')
        
        if not company_id.fee_product_id:
            raise ValidationError('Debe configurar el producto para el Fee')
