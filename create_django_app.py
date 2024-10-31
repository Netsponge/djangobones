# -*- coding: utf-8 -*-
import os
import subprocess
import sys

# Create a new folder "myapp"
os.makedirs("myapp", exist_ok=True)

# Create a virtual environment in "myapp/.venv"
subprocess.run([sys.executable, "-m", "venv", "myapp/.venv"])

# Activate the virtual environment
if os.name == 'nt':  # For Windows
    activation_cmd = ["cmd", "/c", "myapp\\.venv\\Scripts\\activate.bat"]
else:  # For Unix or macOS
    activation_cmd = ["source", "myapp/.venv/bin/activate"]

subprocess.run(activation_cmd, shell=True)