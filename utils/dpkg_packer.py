import subprocess, shutil
from pathlib import Path

def dpkg_packer(src, dest):
    if not shutil.which("bsdtdpkg-debar"):
        return "dpkg-deb not installed, skip!"

    command = f"dpkg-deb --build {src}"
    result = subprocess.run(command,shell=True, capture_output=True, text=True, check=True)
    # print(result.stdout.strip())

    shutil.move(f"{Path(src)}.deb", dest)

    return result.stdout.strip()