from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.product'
    x_cod_fornitore = fields.Char(
        string="Cod. Fornitore"
    )

    x_saldi_prod = fields.Integer(string="Giacienza", readonly=True)