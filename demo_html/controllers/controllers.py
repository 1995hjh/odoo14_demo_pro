from odoo import http
import os
import jinja2
from odoo.http import request

jinja_path = os.path.relpath(os.path.join(os.path.dirname(__file__), '../views'))
loader = jinja2.FileSystemLoader(jinja_path)
jinja_env = jinja2.Environment(loader=loader)


class DemoHtml(http.Controller):

    @http.route('/demo_html/raw/', auth='none')
    def demo_html(self):
        html_path = os.path.relpath(os.path.join(os.path.dirname(__file__), '../views/demo.html'))
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()

    #@http.route('/demo_html/demo_form', auth='none', csrf=False)
   # def demo_form(self, password):
    #    return password

    @http.route('/demo_html/jinja', auth='user')
    def demo_jinja(self):
        template = jinja_env.get_template('jinja.html')
        return template.render({
            'request': request,
            'ars': range(100)
        })

    @http.route('/demo_html/formJinja', auth='none')
    def demo_form(self, password):
        return password

    @http.route('/demo_html/qweb', auth='user')
    def demo_qweb(self):
        return request.render('demo_html.listing', {
            'request': request,
            'ars': range(1000)
        })

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
