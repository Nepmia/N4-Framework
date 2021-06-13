import re
from pathlib import Path
from termcolor import colored

def variable_writer(file, variable_name, variable_content):
    pass

def variable_extractor(file, expression):
    try:
        raw_read = Path(file).read_text()
        var_match = re.search(expression, raw_read)
        var_content = var_match[0].replace("$", "").replace("_", " ").replace("-", " ").replace("{","").replace("}","")
        return var_content
    except TypeError:
        print(
            colored("[N4] ", "blue"),
            colored("TypeError !", "red"),
            colored(" This error can be caused by a messed variable name. Varriable should be"),
            colored(" ${ContentWithNoSpaceBut_or-Instead}", "green")
            )






