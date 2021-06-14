import app
# from template_registrator import templates_module, templates_exporter, template_registrator
from jinja2 import Environment, select_autoescape, FileSystemLoader
import os


env = Environment(
    loader=FileSystemLoader(app.TEMPLATE_FOLDER),
    autoescape=select_autoescape()
)

# template_registrator()
templates_list = os.listdir(app.TEMPLATE_FOLDER)
for template in templates_list:
    temp = env.get_template(template)
    print(temp.render(kek="LOL"))
# env.render_templates(settings.APP_TEMPLATE_FOLDER,  zip=None, )