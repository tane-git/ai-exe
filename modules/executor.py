import subprocess


def execute_command(command):
    print(f"executing: {command}")

    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    stdout, stderr = process.communicate()

    stdout = stdout.decode("utf-8")
    stderr = stderr.decode("utf-8")

    if stdout == "":
        print("stdout is None")
        stdout = "Message from AI-exector: Your command was executed successfully but did not contain any output. Please continue sending commands."

    return stdout, stderr
