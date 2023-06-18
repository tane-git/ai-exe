import subprocess


def execute_command(command):
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    stdout, stderr = process.communicate()

    stdout = stdout.decode("utf-8")
    stderr = stderr.decode("utf-8")

    return stdout, stderr
