# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo import tools

class report_sale_imagen(models.Model):
	_inherit ='sale.order.line'

	time_delivery = fields.Text(string = "Tiempo entrega", index=True)