# -*- coding: utf-8 -*-
import logging
import re

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError
from odoo.osv import expression

from odoo.addons import decimal_precision as dp

from odoo.tools import float_compare, pycompat

class report_sale_imagen(models.Model):
	_inherit ='sale.order.line'

	time_delivery = fields.Text(string = "Tiempo entrega", index=True)

	image = fields.Binary(string="Imagen", related='product_id.product_tmpl_id.image_small',
        help="Small-sized image of the product. It is automatically "
             "resized as a 64x64px image, with aspect ratio preserved. "
             "Use this field anywhere a small image is required.")

	


class purchase_orde_img(models.Model):
	_inherit = 'purchase.order.line'

	img_purchase = fields.Binary(string="Imagen", related='product_id.image_small',
        help="Small-sized image of the product. It is automatically "
             "resized as a 64x64px image, with aspect ratio preserved. "
             "Use this field anywhere a small image is required.")