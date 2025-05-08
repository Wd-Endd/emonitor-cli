import subprocess

def catch_system(command): 
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        check=True,
    )

    return result.stdout.strip()