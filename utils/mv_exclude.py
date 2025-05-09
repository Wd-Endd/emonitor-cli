import shutil, os

def mv_exclude(src, dest, exclude):
    for item in os.listdir(src):
        if item in exclude:
            continue

        shutil.move(src / item, dest / item)