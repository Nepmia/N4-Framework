from jinja2 import Environment, select_autoescape, FileSystemLoader
import app
import os
from termcolor import colored

j_env = Environment(
    loader=FileSystemLoader(app.TEMPLATE_FOLDER),
    autoescape=select_autoescape()
)

def templates_lister():
    print(
    colored("[N4] ", "blue"),
    colored("template list rendered. ", "cyan")
    )
    return os.listdir(app.TEMPLATE_FOLDER)

def template_builder():
    tlist = templates_lister()
    for template in tlist:
        print(
    colored("[N4] ", "blue"),
    colored("Detected template:", "cyan"),
    colored(template, "red"),
    colored("buidling in progress...", "cyan")
    )
    temp = j_env.get_template(template)
    rendered_template = temp.render(kek="LOL")

