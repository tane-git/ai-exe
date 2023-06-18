import subprocess


def execute_command(command):
    try:
        proc = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        return proc.stdout.strip(), proc.stderr.strip()

    except subprocess.CalledProcessError as e:
        return e.stdout.strip(), e.stderr.strip()
