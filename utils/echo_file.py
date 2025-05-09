import shutil, os

def echo_file(target, data):
    with open(target, "a") as f:
        f.write(f"{data}\n")
