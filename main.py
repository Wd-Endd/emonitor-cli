from utils.echo_file import echo_file
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
    depends = "procps"
    description = "Endd's first dpkg"
    installed_size = catch_system(f"du -ks {SCRIPT_DIR} | awk '{{ print $1 }}'")

# print(Control.installed_size)

reset_dir(DIST_DIR)
reset_dir(BUILD_DIR)
cp_items(SCRIPT_DIR, DIST_DIR)
reset_dir(Path(DIST_DIR) / "DEBIAN")

echo_file(Path(DIST_DIR) / "DEBIAN" / "control",f"Package: {Control.name}")
echo_file(Path(DIST_DIR) / "DEBIAN" / "control",f"Architecture: {Control.arch}")
echo_file(Path(DIST_DIR) / "DEBIAN" / "control",f"Maintainer: {Control.maimtainer}")
echo_file(Path(DIST_DIR) / "DEBIAN" / "control",f"Version: {Control.version}")
echo_file(Path(DIST_DIR) / "DEBIAN" / "control",f"Homepage: {Control.homepage}")
echo_file(Path(DIST_DIR) / "DEBIAN" / "control",f"Depends: {Control.depends}")
echo_file(Path(DIST_DIR) / "DEBIAN" / "control",f"Description: {Control.description}")
echo_file(Path(DIST_DIR) / "DEBIAN" / "control",f"Installed-Size: {Control.installed_size}")