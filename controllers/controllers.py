# -*- coding: utf-8 -*-
from odoo import http

# class VerificacionesDeProductos(http.Controller):
#     @http.route('/verificaciones_de_productos/verificaciones_de_productos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/verificaciones_de_productos/verificaciones_de_productos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('verificaciones_de_productos.listing', {
#             'root': '/verificaciones_de_productos/verificaciones_de_productos',
#             'objects': http.request.env['verificaciones_de_productos.verificaciones_de_productos'].search([]),
#         })

#     @http.route('/verificaciones_de_productos/verificaciones_de_productos/objects/<model("verificaciones_de_productos.verificaciones_de_productos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('verificaciones_de_productos.object', {
#             'object': obj
#         })