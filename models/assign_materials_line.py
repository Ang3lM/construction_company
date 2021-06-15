# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AssignMaterialsLine(models.Model):
    _name = 'cc.assign.materials.line'
    _description="Registrar los materiales de las Edificaciones"

    @api.depends('quantity', 'price_unit', 'tax_id')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            price = line.price_unit
            taxes = line.tax_id.compute_all(price, line.currency_id, line.quantity, product=line.product_id, partner=None)
            line.update({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })


    currency_id = fields.Many2one('res.currency')
    product_id = fields.Many2one('product.product', string="Productos")
    name = fields.Text(string='Description', required=True)
    quantity = fields.Integer(string="Cantidad",required=True, default=1.0)
    tax_id = fields.Many2many('account.tax', string="impuesto")
    price_unit = fields.Float(string="Precio",required=True,)
    price_tax = fields.Float(compute='_compute_amount', string='Total Tax', readonly=True, store=True)
    price_total = fields.Monetary(compute='_compute_amount', string='Total', readonly=True, store=True)
    price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal', readonly=True, store=True)
    assign_materials_id = fields.Many2one('cc.assign.materials',string="assign materials")
    

    @api.onchange('product_id')
    def get_price_unit(self):
        self.price_unit = self.product_id.lst_price
        self.name = self.product_id.get_product_multiline_description_sale()
        print("get_price_unittttttttttttttttttttttt")
        print("get_price_unittttttttttttttttttttttt")
        print(self.name)