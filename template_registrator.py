import os
import app
from termcolor import colored
from write import write
import re
from pathlib import Path
from template_handler import templates_lister

def template_registrator():
    module_path = f"{app.MODULE_FOLDER}/TemplateRegistrator/templates.js"
    print(
        colored("[N4] ", "blue"),
        colored("Begining TemplateRegistrator module...", "cyan")
        )
    print(
        colored("[N4] ", "blue"),
        colored("Module folder is", "cyan"),
        colored(module_path, "red")
        )
    templates_list = templates_lister()
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
        title = title_extractor(f"{app.TEMPLATE_FOLDER}/{item}", app.VAR_CATCH_RE, "")
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
    print(
                colored("[N4] ", "blue"),
                colored("Finished to build template list for InstantNav, building pages..", "cyan")
            )


def title_extractor(file, expression, variable_name):
    print(
        colored("[N4] ", "blue"),
        colored("Extracting variable...", "cyan"),
        )
    try:
        raw_read = Path(file).read_text()
        if variable_name == "":
            print(
                colored("[N4] ", "blue"),
                colored("Detected no variable name, assuming it's a title...", "cyan"),
                )
            var_match = re.search(expression, raw_read)
            var_content = var_match[0].replace("$", "").replace("_", " ").replace("-", " ").replace("{","").replace("}","")
            print(
                colored("[N4] ", "blue"),
                colored(var_content, "red"),
                colored("extracted.", "cyan")
                )
            return var_content
        else:
            print(
                colored("[N4] ", "blue"),
                colored("Variable name detected, extracting:", "cyan"),
                colored(variable_name,"red")
                )
            var_match = re.search(fr"\${{({variable_name})}}", raw_read)
            var_content = var_match[0].replace("$", "").replace("_", " ").replace("-", " ").replace("{","").replace("}","")
            print(
                colored("[N4] ", "blue"),
                colored(var_content, "red"),
                colored("extracted.", "cyan")
                )
            return var_content
            
    except TypeError:
        print(
            colored("[N4] ", "blue"),
            colored("TypeError!", "red"),
            colored("This error can be caused by a messed variable name / syntax. Varriable syntax should be", "cyan"),
            colored(" ${ContentWithNoSpaceBut_or-Instead}", "green")
            )