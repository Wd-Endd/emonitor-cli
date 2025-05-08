import os, shutil

def reset_dir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)

    os.mkdir(dir)