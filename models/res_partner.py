from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    percentage_fee = fields.Float(string='% Fee')