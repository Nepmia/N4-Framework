import os
import settings
from termcolor import colored
from write import write
from variable_handler import variable_extractor

def template_registrator():
    module_path = f"{settings.APP_MODULE_FOLDER}/TemplateRegistrator/templates.js"
    print(
        colored("[N4] ", "blue"),
        colored("Begining TemplateRegistrator module...", "cyan")
        )
    print(
        colored("[N4] ", "blue"),
        colored("Module folder is", "cyan"),
        colored(module_path, "red")
        )
    templates_list = os.listdir(settings.APP_TEMPLATE_FOLDER)
    templates_module(module_path)
    templates_exporter(templates_list, module_path)



def templates_module(module_path):
    base_template = "const Templates = {\n"
    print(
        colored("[N4] ", "blue")
        ,colored("Testing", "cyan")
        ,colored("template.js", "red")
        )
    if os.path.exists(module_path):
        print(
            colored("[N4] ", "blue"),
            colored("test positive, clearing content to rewrite updated templates list...", "cyan")
            )
        os.remove(module_path)
        write(module_path, base_template, "w")
    else:
        print(
            colored("[N4] ", "blue"),
            colored("test negaticve, creating and writing templates list", "cyan")
            )
        write(module_path, base_template, "w")


def templates_exporter(templates_list, module_path):
    for item in templates_list:
        title = variable_extractor(f"{settings.APP_TEMPLATE_FOLDER}/{item}", settings.VAR_CATCH_RE, "")
        parsed_item = item.replace(".html", "")
        if title == None:
            print(
                colored("[N4] ", "blue"),
                colored("Given value is incorect, skipping.", "cyan")
            )
            pass
        else:
            write(module_path, f"    {parsed_item} : \"{title}\",\n", "a")
    write(module_path, "},", "a")