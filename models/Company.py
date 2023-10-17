from odoo import models, fields, api

class Company(models.Model):
    _inherit = 'res.company'
    x_acc_number = fields.Many2one(
        'res.partner.bank', 
        string="Banca", 
    )

    # x_name_bank = fields.Char( enable=0  )
    
    # @api.onchange('x_acc_number')
    # def onchange_x_acc_number(self):
    #     if self.x_acc_number:
    #         self.x_name_bank = self.x_acc_number.name
    #     else:
    #         self.acc_number = ''