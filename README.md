
# AI Inference on Mobile Devices

## Setup Instructions


1. **Install Python 3.11.8**
	- Make sure you are using Python version 3.11.8. You can manage multiple Python versions with [pyenv-win](https://github.com/pyenv-win/pyenv-win) or your preferred tool.


2. **Create a `.env` file with your Qualcomm API Key**
	 - In the project root, create a file named `.env` with the following content:

		 ```env
		 ai_hub_api_token=YOUR_QUALCOMM_API_KEY_HERE
		 ```



3. **Install dependencies**
	 - Download the [certifi certificate bundle](https://pypi.org/project/certifi/) if you don't already have it. You can find the path to the installed `cacert.pem` with:

		 ```sh
		 python -m certifi
		 ```

	 - Open a terminal in the project directory and run:

		 ```sh
		 pip install qai-hub-models torchinfo scikit-image --cert "C:\Users\vandang\.pyenv\pyenv-win\certifi\cacert.pem"
		 ```

	 - Adjust the `--cert` path if your certificate is located elsewhere, or omit it if not needed.

	 > **Note for Zscaler or corporate firewall users:**
	 >
	 > If you are behind a Zscaler (or similar) firewall, you must append your organization's Zscaler root certificate to the end of the `cacert.pem` file used above (e.g., `C:\Users\vandang\.pyenv\pyenv-win\certifi\cacert.pem`). This allows Python and pip to trust your proxy for HTTPS connections. Contact your IT department to obtain the Zscaler root certificate if needed.


4. **You're ready!**
	- Run the provided scripts to perform model export, inference, or other tasks as described in the code and documentation.


---

**Important Note**

>
> This repository is based on source code originally copied from the [DeepLearning.AI Short Course: Introduction to On-Device AI](https://www.deeplearning.ai/short-courses/introduction-to-on-device-ai/). Significant changes and enhancements have been made, but the foundation comes from that course.

For more details, see the comments in each script or reach out to the project maintainer.