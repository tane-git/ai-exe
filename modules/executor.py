import subprocess


def execute_command(command):
    print(f"executing: {command}")

    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    stdout, stderr = process.communicate()

    return stdout.decode("utf-8"), stderr.decode("utf-8")
