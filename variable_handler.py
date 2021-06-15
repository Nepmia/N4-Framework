import re
from pathlib import Path
from termcolor import colored

def variable_extractor(file, expression, variable_name):
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
