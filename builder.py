import os
import settings

def template_registrator():
    module_path = f"{settings.APP_ROOT}/modules/TemplateRegistrator/templates.js"
    templates_list = os.listdir(settings.APP_TEMPLATE_FOLDER)
    templates_module(module_path)
    templates_exporter(templates_list, module_path)

def templates_module(module_path):
    if os.path.exists(module_path):
        print("module found, deleting")
        os.remove(module_path)
    else:
        print("module not found, creating")
        open(module_path, 'a').close()


def templates_exporter(templates_list, module_path):
    for item in templates_list:
        with open(module_path, "a") as module:
            module.write(item)

template_registrator()

            


