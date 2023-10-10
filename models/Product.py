from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    x_cod_fornitore = fields.Many2one(
        'res.partner', 
        string="Fornitore", 
        domain="[('display_name', '!=', False)]"
    )

    x_saldi_prod = fields.Integer(string="Giacienza", readonly=True)
    
