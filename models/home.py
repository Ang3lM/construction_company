# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Home(models.Model):
    _name = 'cc.home'
    _rec_name='type_home'
    _description="Registrar la informacion de las casa"

    image_home = fields.Binary(string="image")
    type_home = fields.Char(required=True)
    lst_price = fields.Float(string="Precio de venta",required=True)
    