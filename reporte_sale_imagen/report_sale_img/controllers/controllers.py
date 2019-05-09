# -*- coding: utf-8 -*-
from odoo import http

# class ReportSaleImg(http.Controller):
#     @http.route('/report_sale_img/report_sale_img/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_sale_img/report_sale_img/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_sale_img.listing', {
#             'root': '/report_sale_img/report_sale_img',
#             'objects': http.request.env['report_sale_img.report_sale_img'].search([]),
#         })

#     @http.route('/report_sale_img/report_sale_img/objects/<model("report_sale_img.report_sale_img"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_sale_img.object', {
#             'object': obj
#         })