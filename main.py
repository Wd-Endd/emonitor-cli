from utils.pacman_packer import pacman_packer
from utils.mv_exclude import mv_exclude
from utils.dpkg_packer import dpkg_packer
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
DEB_DIR = Path(DIST_DIR) / "deb"
PACMAN_DIR = Path(DIST_DIR) / "pacman"

class Control:
    name = "emonitor-cli"
    arch = "all"
    pacman_arch = "any"
    maimtainer = "Wd-Endd <noreply@github.com>"
    version = "1.0.4"
    release = 0
    homepage = "https://github.com/Wd-Endd/emonitor-cli.git"
    depends = ["procps", "bc"]
    description = "Endd's first dpkg"
    installed_size = catch_system(f"du -ks {SCRIPT_DIR} | awk '{{ print $1 }}'")
    build_date = catch_system("date +%s")

# print(Control.installed_size)

reset_dir(DIST_DIR)
reset_dir(BUILD_DIR)
reset_dir(DEB_DIR)
reset_dir(PACMAN_DIR)

cp_items(SCRIPT_DIR, DEB_DIR)
cp_items(SCRIPT_DIR, PACMAN_DIR)

reset_dir(Path(DEB_DIR) / "DEBIAN")
echo_file(Path(DEB_DIR) / "DEBIAN" / "control", f"Package: {Control.name}")
echo_file(Path(DEB_DIR) / "DEBIAN" / "control", f"Architecture: {Control.arch}")
echo_file(Path(DEB_DIR) / "DEBIAN" / "control", f"Maintainer: {Control.maimtainer}")
echo_file(Path(DEB_DIR) / "DEBIAN" / "control", f"Version: {Control.version}")
echo_file(Path(DEB_DIR) / "DEBIAN" / "control", f"Homepage: {Control.homepage}")
echo_file(Path(DEB_DIR) / "DEBIAN" / "control", f"Depends: {', '.join(Control.depends)}")
echo_file(Path(DEB_DIR) / "DEBIAN" / "control", f"Description: {Control.description}")
echo_file(Path(DEB_DIR) / "DEBIAN" / "control", f"Installed-Size: {Control.installed_size}")
os.system(f"chmod +0755 {Path(DEB_DIR) / "DEBIAN"}")

echo_file(Path(PACMAN_DIR) / ".PKGINFO", f"pkgname = {Control.name}")
echo_file(Path(PACMAN_DIR) / ".PKGINFO", f"pkgbase = {Control.name}")
echo_file(Path(PACMAN_DIR) / ".PKGINFO", f"pkgver = {Control.version}-{Control.release}")
echo_file(Path(PACMAN_DIR) / ".PKGINFO", f"pkgdesc = {Control.description}")
echo_file(Path(PACMAN_DIR) / ".PKGINFO", f"url = {Control.homepage}")
echo_file(Path(PACMAN_DIR) / ".PKGINFO", f"builddate = {Control.build_date}")
echo_file(Path(PACMAN_DIR) / ".PKGINFO", f"packer = {Control.maimtainer}")
echo_file(Path(PACMAN_DIR) / ".PKGINFO", f"size = {Control.installed_size}")
echo_file(Path(PACMAN_DIR) / ".PKGINFO", f"arch = {Control.pacman_arch}")
echo_file(Path(PACMAN_DIR) / ".PKGINFO", "license = MIT")
for depend in Control.depends:
  echo_file(Path(PACMAN_DIR) / ".PKGINFO", f"depend = {depend}") 

dpkg_packer(DEB_DIR, Path(BUILD_DIR) / f"{Control.name}-{Control.version}-{Control.arch}.deb")
pacman_packer(PACMAN_DIR, Path(BUILD_DIR) / f"{Control.name}-{Control.version}-{Control.pacman_arch}.pkg.tar.zst")

mv_exclude(
    DEB_DIR,
    Path(DEB_DIR) / "data" / "data" / "com.termux" / "files",
    [ "DEBIAN" ],
)

mv_exclude(
    PACMAN_DIR,
    Path(PACMAN_DIR) / "data" / "data" / "com.termux" / "files",
    [ ".PKGINFO" ],
)

dpkg_packer(DEB_DIR, Path(BUILD_DIR) / f"{Control.name}-{Control.version}-termux-{Control.arch}.deb")
pacman_packer(PACMAN_DIR, Path(BUILD_DIR) / f"{Control.name}-{Control.version}-termux-{Control.pacman_arch}.pkg.tar.zst")