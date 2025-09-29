from odoo import fields, models


class SaleOrderTemplate(models.Model):
    _inherit = 'sale.order.template'

    fee_calc = fields.Boolean(
        string='Obligar cálculo de Fee', 
        help="Al confirmar una orden de venta, se controlará que la línea del Fee esté presente"
    )