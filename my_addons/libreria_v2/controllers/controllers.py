# from odoo import http


# class LibreriaV2(http.Controller):
#     @http.route('/libreria_v2/libreria_v2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libreria_v2/libreria_v2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('libreria_v2.listing', {
#             'root': '/libreria_v2/libreria_v2',
#             'objects': http.request.env['libreria_v2.libreria_v2'].search([]),
#         })

#     @http.route('/libreria_v2/libreria_v2/objects/<model("libreria_v2.libreria_v2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libreria_v2.object', {
#             'object': obj
#         })

