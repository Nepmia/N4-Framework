from termcolor import colored
import sys

basic_answers =  {
        "yes" : True,
        "y" : True,
        "no" : False,
        "n" : False,
}

basic_no_default = "[y/N]"
basic_yes_default = "[Y/n]"

def  N4_println(message:str, important_or_dangerous:str = "", optional_message:str = ""):
    """N4 CLI Printing function. Prints a message in the terminal.

    Args:
        message (str):  Message to print, commonly str.
        important_or_dangerous (str, optional): Important or dangerous information that needs to be in red for the user to notice it. Defaults to None.
        optional_message (str, optional): Optional message after an error or an important info. Defaults to None.
    """
    print(
        colored("[N4] ", "blue"),
        colored(message, "cyan"),
        colored(important_or_dangerous,"red"),
        colored(optional_message, "cyan"),
     )

def N4_user_prompt(valid_answers:dict, question:str, display_answer:str, default:str = None) -> str: 
    """N4 CLI user interaction method. Allow N4 to ask questions to the user and alter N4 behavior.

    Args:
        valid_answers (dict): a dict of the valid answers (yes : true, no : false, y : true, n : false, maybe : maybe, idk : thing).
        question (str): The question you ask to the user.
        display_answer (str): The possible answers you'll show to the user (like: [Y/n]).
        default (str, optional): Default answer that will be given if the user just press enter without entering any answer, is optional. Defaults to None.

    Returns:
        str: The value of the key of valid_answers that the user gave. 
    """

    N4_println(question)
    N4_println("Please answer with:", display_answer)
    while True:
        user_answer = input().lower()
        if user_answer == "" and default is not None:
            return default
        elif user_answer in valid_answers:
            return valid_answers[user_answer]
        else:
            N4_println("Incorect answer.", "Please retry. \n")
            N4_println(question)
            N4_println("Please answer with:", display_answer)

def  prompt_tester():
    """Will ask a question to the user with possible answers to test if N4_user_prompt is working correctly.
    """
    N4_println("Beginning prompt input test. Valid answers will be:", "Yes or No", "Result will be a sentence containing the answer.")

    prompt = N4_user_prompt(basic_answers, "Are you aware that this is a test?",basic_no_default, "no")

    if prompt is True:
        N4_println("Yes! You knew it! Wellplayed!")
    else:
        N4_println("Boo... Big noob!")
