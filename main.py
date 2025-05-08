from utils.create_build import create_build
from utils.create_dist import create_dist

DIST_DIR = "./dist"
BUILD_DIR = "./.build"
SCRIPT_DIR = "./script"

class Control:
    name = "emonitor-cli",
    arch = "all",
    maimtainer = "Wd-Endd <noreply@github.com>",
    version = 1.0,
    homepage = "https://github.com/Wd-Endd/emonitor-cli.git",
    depend = "none", # default
    description = "Endd's first dpkg",
    installed_size = 0, # default

create_dist(DIST_DIR)
create_build(BUILD_DIR)