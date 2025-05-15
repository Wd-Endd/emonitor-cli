# from pathlib import Path
import subprocess, os, shutil
def pacman_packer(src, dest):
    if not shutil.which("bsdtar"):
        return "bsdtar not installed, skip!"

    items = " ".join(os.listdir(src))

    command = f"cd {src}; bsdtar -czf {dest} --format=ustar {items}"
    # print(command)
    result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
    return result