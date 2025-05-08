from pathlib import Path
import shutil, os

def cp_items(src, dest):
    for item in os.listdir(src):
        src_item = Path(src) / item
        dest_item = Path(dest) / item

        shutil.copytree(src_item, dest_item)