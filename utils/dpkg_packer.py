import subprocess, shutil
from pathlib import Path

def dpkg_packer(src, dest):
    command = f"dpkg-deb --build {src}"
    result = subprocess.run(command,shell=True, capture_output=True, text=True, check=True)
    # print(result.stdout.strip())

    shutil.move(f"{Path(src)}.deb", dest)

    return result.stdout.strip()