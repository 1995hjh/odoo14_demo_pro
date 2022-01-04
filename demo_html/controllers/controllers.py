from odoo import http
import os

class DemoHtml(http.Controller):
    @http.route('/demo_html/raw/', auth='none')
    def demo_html(self):
        html_path = os.path.relpath(os.path.join(os.path.dirname(__file__), '../views/demo.html'))
        with open(html_path) as f:
            return f.read()
#         return "Hello, world"

#     @http.route('/demo_html/demo_html/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_html.listing', {
#             'root': '/demo_html/demo_html',
#             'objects': http.request.env['demo_html.demo_html'].search([]),
#         })

#     @http.route('/demo_html/demo_html/objects/<model("demo_html.demo_html"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_html.object', {
#             'object': obj
#         })
