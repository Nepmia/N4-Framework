import os
import app
from termcolor import colored
from write import write
import re
from pathlib import Path
from template_handler import templates_lister

def template_registrator():
    """Get templateRegistrator module path and call template module and exporter functions
    """
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
    """Tests if template.js exists and clear it then rewrites a blank const template

    Args:
        module_path (string): path to templateRegistrator module
    """
    base_template = "const Templates = {\n" # Basic JS const list template
    print(
        colored("[N4] ", "blue")
        ,colored("Testing", "cyan")
        ,colored("template.js", "red")
        )
    if os.path.exists(module_path): # Test if template.js already exists, if it does then it clears it.
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
    """Writes template.js by extracting titles of templates in template_list. It writes them in a js list like  "home" : Tiltle,  "page": Title and then close the list. 

    Args:
        templates_list (list): List containing templates file names 
        module_path (string): path to templateRegistrator module
    """
    for item in templates_list:
        title = title_extractor(f"{app.PAGES_FOLDER}/{item}") # Get template title using title_extractor()
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


def title_extractor(file):
    """Extracts titles from template using regex

    Args:
        file (string): path to the file the function need to work on, usually a template 

    Returns:
        [string]: return a correctly parsed title so it can be writen in template.js
    """
    print(
        colored("[N4] ", "blue"),
        colored("Extracting title of", "cyan"),
        colored(file,"red")
        )
    try:
        raw_read = Path(file).read_text()
        var_match = re.search(app.PAGE_TITLE_REGEX, raw_read)
        var_content = var_match[0].replace("pageTitle=", "").replace("_", " ").replace("-", " ").replace("\"","")
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
            colored("Couldn't extract the title, make sure it respect the syntax as following:", "cyan"),
            colored("pageTitle=\"YourTitle\"", "green")
            )