from utils.reset_dir import reset_dir
from pathlib import Path

DIST_DIR = Path("./dist").absolute()
BUILD_DIR = Path("./.build").absolute()
SCRIPT_DIR = Path("./script").absolute()

class Control:
    name = "emonitor-cli",
    arch = "all",
    maimtainer = "Wd-Endd <noreply@github.com>",
    version = 1.0,
    homepage = "https://github.com/Wd-Endd/emonitor-cli.git",
    depend = "none", # default
    description = "Endd's first dpkg",
    installed_size = 0, # default

reset_dir(DIST_DIR)
reset_dir(BUILD_DIR)