from termcolor import colored

def  N4_println(message:any, important_or_dangerous:any = None, optional_message:any = None):
    """N4 CLI Printing function. Prints a message in the terminal.

    Args:
        message (any):  Message to print, commonly str.
        important_or_dangerous (any, optional): Important or dangerous information that needs to be in red for the user to notice it. Defaults to None.
        optional_message (any, optional): Optional message after an error or an important info. Defaults to None.
    """
    print(
        colored("[N4] ", "blue"),
        colored(message, "cyan"),
        colored(important_or_dangerous,"red"),
        colored(optional_message, "cyan"),
     )