# Register Qualcomm AI hub, then obtain the API key from https://app.aihub.qualcomm.com/account

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

# Set output_dir to the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.argv = [sys.argv[0], f"--output-dir={script_dir}"]
runpy.run_module("qai_hub_models.models.ffnet_40s.demo", run_name="__main__")
