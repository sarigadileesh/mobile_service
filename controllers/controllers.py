# -*- coding: utf-8 -*-
# from odoo import http


# class MobileService(http.Controller):
#     @http.route('/phone_shop/phone_shop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/phone_shop/phone_shop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('phone_shop.listing', {
#             'root': '/phone_shop/phone_shop',
#             'objects': http.request.env['phone_shop.phone_shop'].search([]),
#         })

#     @http.route('/phone_shop/phone_shop/objects/<model("phone_shop.phone_shop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('phone_shop.object', {
#             'object': obj
#         })
