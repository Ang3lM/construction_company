# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

from odoo import fields
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.addons.portal.controllers.web import Home
import logging
import json

_logger = logging.getLogger(__name__)


class CustomerPortal(CustomerPortal):

    @http.route(['/my', '/my/home'], type='http', auth="user", website=True)
    def home(self, **kw):

        home = request.env['cc.home'].sudo().search([])
        # print(request.session)
        values = {
            'homes': home
        }

        return http.request.render('construction_company.clientess', values)


class Home(Home):    
    # validacion
    # @http.route('/',type='http', auth="public", website=True)
    # def home(self,*args, **kw):
    #     client = request.env['cc.client']
    #     product = request.env['product.product'].sudo().search([])
    #     print(product)
    #     values = {
    #         'products': product
    #     }
    #     return http.request.render('cc.client',values)
    
        
    # @http.route('/web/login', type='http', auth="none", sitemap=False)
    # def web_login(self, redirect=None, **kw):
    #     if not redirect:
    #         redirect="/"
    #     #~ redirect="/profile"
    #     return super(Home, self).web_login(redirect=redirect,kw=kw)

    def practiica(self):
        print("sdfsdfsdfsdf")