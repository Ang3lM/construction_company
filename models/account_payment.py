# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class account_payment(models.Model):
    _inherit = "account.payment"



    def action_validate_invoice_payment(self):
    	record = super(account_payment,self).action_validate_invoice_payment()

    	print("Se hizo el primer pagooooooooooooooooooooooooooooooo")
    	print("Se hizo el primer pagooooooooooooooooooooooooooooooo")
    	print("Se hizo el primer pagooooooooooooooooooooooooooooooo")
    	return record