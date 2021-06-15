# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class AssignMaterials(models.Model):
    _name = 'cc.assign.materials'
    _description="Registrar la informacion de los materiales"


    @api.depends('assign_materials_line_ids.price_total')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for record in self:
            amount_untaxed = amount_tax = 0.0
            for line in record.assign_materials_line_ids:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            record.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax,
            })

    currency_id = fields.Many2one('res.currency')
    home_id = fields.Many2one('cc.home',string="Tipo de casa",required=True)
    amount_untaxed = fields.Monetary(string='Base imponible', store=True, readonly=True, compute='_amount_all', track_visibility='onchange', track_sequence=5)
    amount_tax = fields.Monetary(string='Impuestos', store=True, readonly=True, compute='_amount_all')
    amount_total = fields.Monetary(string='Total', store=True, readonly=True, compute='_amount_all', track_visibility='always', track_sequence=6)
    assign_materials_line_ids = fields.One2many('cc.assign.materials.line','assign_materials_id',string="assign materials line")
