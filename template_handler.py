from ast import Index
from jinja2 import Environment, select_autoescape, FileSystemLoader
import app
import os
import app.components 
import re

from helpers import N4_println, working_dir

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

                for item in template_match:
                    component_name = re.findall(r"^(.*?) ", item)[0]
                    component_arg = re.findall(r" (\w+=\".+?\")", item)

                    if component_name in app.components.COMPONENT_LIST:
                        N4_println("Yes!")

                        parsed_arg_list = str(component_arg).replace("[","").replace("]","").replace("'","")
                        component_path = f"{app.COMPONENT_FOLDER}/{component_name}/{component_name}/{component_name}.html"
                        parsed_component = f"{{% with {parsed_arg_list} %}}{{% include \"{component_path}\" %}}{{% endwith %}}"
                        test = re.sub(fr"<(({component_name}).+)\s+/>", parsed_component, openned_template)

                        N4_println(test)


                    else:
                        N4_println("No!")


        temp = j_env.get_template(test)
        rendered_template = temp.render()
        N4_println(rendered_template)

def component_builder():
    for component in app.COMPONENT_FOLDER:
        pass