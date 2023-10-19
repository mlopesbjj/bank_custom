from odoo import models, fields, api

class ResPartnerBank(models.Model):
    print('executou a parada 1.')
    _inherit = 'res.partner.bank'
    x_acc_number = fields.Many2one(
        'res.partner.bank', 
        string="N. Banca", 
        domain="[('acc_number', '!=', False)]" 
    )
    
    # acc_number = fields.Char(
    #     # string='.',
    #     invisible=,
    #     required=0
    # )

    # @api.onchange('x_acc_number')
    # def onchange_x_acc_number(self):
    #     print('executou a parada 2.')
    #     if self.x_acc_number:
    #         self.acc_number = self.x_acc_number.acc_number
    #     else:
    #         self.acc_number = ''