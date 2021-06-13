import os
import settings
import re
from termcolor import colored
from pathlib import Path
from TemplateRegistrator import template_registrator, templates_exporter, templates_module

def write(path, content, method):
    print(
        colored("[N4] ", "blue"),
        colored("Recorded a writing request with content:", "cyan"),
        colored(content, "red"), colored("with method", "cyan"),colored(method, "red"),
        colored("on this file","cyan"),
        colored(path,"red")
        )
    with open(path, method) as module:
        module.write(content)

template_registrator()

            


