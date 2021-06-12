import os
import settings

def template_registrator():
    module_path = f"{settings.APP_ROOT}/modules/TemplateRegistrator/templates.js"
    templates_list = os.listdir(settings.APP_TEMPLATE_FOLDER)
    templates_module(module_path)
    templates_exporter(templates_list, module_path)

def templates_module(module_path):
    base_template = "const Templates = {\n"
    if os.path.exists(module_path):
        print("module found, deleting")
        os.remove(module_path)
        templates_module_writer(module_path, base_template, "w")
    else:
        print("module not found, creating")
        templates_module_writer(module_path, base_template, "w")

def templates_module_writer(module_path, content, method):
    with open(module_path, method) as module:
        module.write(content)

def templates_exporter(templates_list, module_path):
    for item in templates_list:
        with open(module_path, "a") as module:
            parsed_item = item.replace(".html", "")
            module.write(f"{parsed_item}\n")
    templates_module_writer(module_path, "\n},", "a")


template_registrator()

            


