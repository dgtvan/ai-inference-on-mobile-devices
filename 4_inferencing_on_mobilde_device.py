# Register Qualcomm AI hub, then obtain the API key from https://app.aihub.qualcomm.com/account

#1. Go to https://www.cityscapes-dataset.com/ and make an account
#2. Go to https://www.cityscapes-dataset.com/downloads/ and download `leftImg8bit_trainvaltest.zip` and `gtFine_trainvaltest.zip`
#3. Run `python -m qai_hub_models.datasets.configure_dataset --dataset cityscapes --files /path/to/leftImg8bit_trainvaltest.zip /path/to/gtFine_trainvaltest.zip`

# --- Increase global requests timeout ---
import requests.adapters
old_send = requests.adapters.HTTPAdapter.send
def new_send(self, request, **kwargs):
    print(f"HTTPAdapter.send called with timeout={kwargs.get('timeout')}")
    # Set a higher timeout (e.g., 120 seconds)
    kwargs["timeout"] = 240
    return old_send(self, request, **kwargs)
requests.adapters.HTTPAdapter.send = new_send

import qai_hub
from env_loader import get_environment_variable
import subprocess
import runpy
import sys
import os

ai_hub_api_token = get_environment_variable('ai_hub_api_token')

# Configure qai-hub CLI with the API token
subprocess.run([
    "qai-hub", "configure", "--api_token", ai_hub_api_token
], check=True)


devices = [
    "Samsung Galaxy S22 Ultra 5G",
    "Samsung Galaxy S22 5G",
    "Samsung Galaxy S22+ 5G",
    "Samsung Galaxy Tab S8",
    "Xiaomi 12",
    "Xiaomi 12 Pro",
    "Samsung Galaxy S22 5G",
    "Samsung Galaxy S23",
    "Samsung Galaxy S23+",
    "Samsung Galaxy S23 Ultra",
    "Samsung Galaxy S24",
    "Samsung Galaxy S24 Ultra",
    "Samsung Galaxy S24+",
]

import random
selected_device = random.choice(devices)
print(selected_device)

# Convert Jupyter magic command to Python
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.argv = [
    sys.argv[0],
    f"--device={selected_device}",
    f"--eval-mode=on-device",
    f"--output-dir={script_dir}"
]
runpy.run_module("qai_hub_models.models.ffnet_40s.demo", run_name="__main__")

