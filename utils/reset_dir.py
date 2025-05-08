import os

def reset_dir(dir):
    if os.path.exists(dir):
        os.rmdir(dir)

    os.mkdir(dir)