# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Client(http.Controller):

  @http.route('/client/create', auth="user", type='http' , website=True)
  def clientcreate(self, **post):
    client = request.env['cc.client'].new()
    values = {
      'nui':post['nui'],
      'name':post['name'],
      'surname':post['surname'],
      'phone':post['phone'],
      'direction':post['direction'],
      'home_id':post['home_id'],
    }
    record_create = client.create(values)
    client_data = request.env['cc.client'].sudo().search([])
    client_request = {'clients': client_data}

    user_id = request.env['res.users'].browse(request.session.uid)
    client_reques = {
      'name':record_create.home_id.type_home,
      'user_id':user_id,
      'client':record_create

    }
    request.env['cc.client'].create_request_home(client_reques)
    return http.request.render('construction_company.clientTableTree', client_request)