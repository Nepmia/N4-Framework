from helpers import *

def prompt_tester():
    N4_println("Beginning prompt input test. Valid answers will be:", "Yes or No", "Result will be a sentence containing the answer.")

    valid_answers = {
        "yes": True,
        "y": True,
        "no": False,
        "n": False,
    }
 
    prompt = N4_user_prompt(valid_answers, "Are you aware that this is a test?", "no")
    N4_println("User input is:", prompt)

    sentence = f"You might wanna know that you've been tested! {prompt}"

    N4_println("Here are your results!")
    N4_println("", sentence)

prompt_tester()