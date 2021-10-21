from termcolor import colored

from helpers import N4_println

def write(path:str, content:str, method:str):
    N4_println("Recorded a writing request with content:", content, f"on file {path}")

    with open(path, method) as module:
        module.write(content)