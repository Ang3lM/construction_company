# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Client(models.Model):
  _name = 'cc.client'
  _description="Registrar la informacion del usuario"

  nui = fields.Char(string="Nui",required=True)
  name = fields.Char(string="Nombre",required=True)
  surname = fields.Char(string="Apellido",required=True)
  phone = fields.Char(string="Telefono",size=11,required=True)
  direction = fields.Text(string="Direccion",required=True)
  home_id = fields.Many2one('cc.home',required=True)
  state = fields.Selection(
  	[('approved','Aprobado'),
  	('denied','Denegado')],
  	string="state"
  )


  def create_request_home(self, values):
    name = values.get('name')
    user_id = values.get('user_id')
    client=values.get('client')
    
    crm = self.env['crm.lead'].sudo().create({
      'name':name,
      'partner_id':user_id.partner_id.id,
      'active':True,
      'email_from':user_id.partner_id.email,
      'contact_name':user_id.partner_id.display_name,
      'type':'opportunity',
      'priority':0,
      'stage_id':1,
      'user_id':user_id.id,
      'day_open':1,
      'probability':10,
      'planned_revenue':client.home_id.lst_price,
      'company_id':1
    })


        