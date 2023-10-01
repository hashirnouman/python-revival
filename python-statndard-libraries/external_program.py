import subprocess
complete = subprocess.run(['ls', '-l'], capture_output=True)
print("args ", complete.args)
print("return code ", complete.returncode)
print("stderr ", complete.stderr)
print("stdout ", complete.stdout)
