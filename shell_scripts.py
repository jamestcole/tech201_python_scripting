import os
import subprocess

# Python doesnt't actually ran shell commands
# Instead we can Python to run shell script

script_dir = os.path.dirname(__file__)

script_absolute_path = os.path.join(script_dir + "files/script.sh")

subprocess.call(['sh'], script_absolute_path)