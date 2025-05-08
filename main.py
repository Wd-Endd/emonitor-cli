from utils.catch_system import catch_system
from utils.cp_items import cp_items
from utils.reset_dir import reset_dir
from pathlib import os, Path
import shutil

THIS_DIR = Path("./").absolute()
DIST_DIR = Path("./dist").absolute()
BUILD_DIR = Path("./.build").absolute()
SCRIPT_DIR = Path("./script").absolute()
# SCRIPTS = Path(F"{SCRIPT_DIR}").

class Control:
    name = "emonitor-cli"
    arch = "all"
    maimtainer = "Wd-Endd <noreply@github.com>"
    version = 1.0
    homepage = "https://github.com/Wd-Endd/emonitor-cli.git"
    depend = "none"
    description = "Endd's first dpkg"
    installed_size = catch_system(f"du -ks {SCRIPT_DIR} | awk '{{ print $1 }}'")

print(Control.installed_size)

reset_dir(DIST_DIR)
reset_dir(BUILD_DIR)
cp_items(SCRIPT_DIR, DIST_DIR)