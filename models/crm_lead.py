# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Lead(models.Model):
    _inherit = "crm.lead"


    @api.onchange('stage_id')
    def create_proyect(self):
    	print("create_proyecttttttttttttttttttttttt")
    	print("create_proyecttttttttttttttttttttttt")

    	project = self.env['project.project']
    	# name = 'Construcion de casa tipo ' + self.name
    	user_id = self.user_id
    	project = project.create({
    		'name':self.name,
    		'active':True,
    		'sequence':10,
    		'company_id':1,
    		'label_tasks':'Tareas',
    		'resource_calendar_id':self.partner_id.company_id.resource_calendar_id.id,
    		'user_id':user_id.id,
    		'privacy_visibility':'portal'

    	})

    	self.project_sales(user_id, project)
    	

    def project_sales(self, user_id, project):

    	home = self.env['cc.home'].search([('type_home','=',self.name)])
    	assign_materials = self.env['cc.assign.materials'].search([('home_id','=',home.id)])
    	print("2assign_materialssssssssssssssssssssssssssssss")
    	print("2assign_materialssssssssssssssssssssssssssssss")
    	print(assign_materials.home_id.type_home)
    	print(user_id)

    	order_line = []

    	for record in assign_materials.assign_materials_line_ids:
    		order_line.append((0,0,{
    			'name':record.product_id.product_tmpl_id.name,
    			'invoice_status':'invoiced',
    			'product_id':record.product_id.id,
    			'name':record.name,
    			'quantity':record.quantity,
    			'price_unit':record.price_unit,
    			'tax_id':[(6,0,record.tax_id.ids)],
    			'price_subtotal':record.price_subtotal,
    			'state':'draft',
    			'is_service':False

    		}))

    	print(order_line)
    	sale_order = self.env['sale.order']

    	sale = sale_order.create({
    		'state':'draft',
    		'confirmation_date':fields.Datetime.now(),
    		'user_id':user_id.id,
    		'partner_id':self.partner_id.id,
    		'pricelist_id':1,
    		'invoice_status':'invoiced',
    		'amount_untaxed':assign_materials.amount_untaxed,
    		'amount_tax':assign_materials.amount_tax,
    		'amount_total':assign_materials.amount_total,
    		'order_line':order_line
    	})
    	print(sale.order_line)
    	print(sale)

    	self.task_project_creation(project,sale)

    def task_project_creation(self, project,sale):
    	print("task_project_creationnnnnnnnnnnnnnnnnnnnnnnnnnnn")
    	task = self.env['project.task']
    	print(sale)
    	for record in sale.order_line:
    		name = sale.name + ':' + record.product_id.product_tmpl_id.name
	    	print(name)
	    	print(name)
	    	print(record.product_id.id)
	    	print(record.product_id.product_tmpl_id.name)
	    	task.create({
	    		'name':name,
	    		'active':True,
	    		'sequence':10,
	    		'stage_id':1,
	    		'kanban_state':'normal',
	    		'project_id':project.id,
	    		'partner_id':self.partner_id.id,
	    		'company_id':self.partner_id.company_id.id,
	    		'email_from':self.partner_id.email,
	    		'progress':60,
	    		'sale_line_id':record.id,
	    		'sale_order_id':sale.id,
	    		'billable_type':'task_rate',
	    	})