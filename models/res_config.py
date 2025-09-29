from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    def_percentage_fee = fields.Float(string='% de Fee por defecto')
    fee_product_id  = fields.Many2one('product.product', string='Producto Fee')


class BaseConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def_percentage_fee = fields.Float(related="company_id.def_percentage_fee", readonly=False)
    fee_product_id  = fields.Many2one('product.product', related="company_id.fee_product_id", readonly=False)
