from jinja2 import Environment, select_autoescape, FileSystemLoader
import app
import os
import app.components 
import re

from helpers import N4_println

j_env = Environment(
    loader=FileSystemLoader(app.PAGES_FOLDER),
    autoescape=select_autoescape()
)

def templates_lister():
    """Lists templates in app.TEMPLATE_FOLDER

    Returns:
        [list]: List containing templates file names 
    """
    N4_println("Template list rendered.")
    return os.listdir(app.PAGES_FOLDER)

def template_builder(template_list:list):

    for template in template_list:

        N4_println("Detected template:", template)

        for component in app.components.COMPONENT_LIST:
            N4_println("found component:", component)
            with open(os.path.join(app.PAGES_FOLDER, template), "r") as current_template:
                openned_template = current_template.read()
                N4_println("openned is",openned_template)
                template_match =  re.findall(r"<(.+)\s+/>", openned_template)
                N4_println(template_match)


        temp = j_env.get_template(template)
        rendered_template = temp.render(kek="LOL")
        N4_println(rendered_template)

def component_builder():
    for component in app.COMPONENT_FOLDER:
        pass
