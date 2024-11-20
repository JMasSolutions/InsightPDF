#main.py

import os
import subprocess

# Set up environment variables for model paths and other requirements
os.environ["PATH"] = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:" + os.environ.get("PATH", "")
os.environ["MODEL_CACHE_DIR"] = os.path.expanduser("~/.cache/huggingface/transformers")  # Set model cache directory

# Ensure the model cache directory exists
model_path = os.path.join(os.environ["MODEL_CACHE_DIR"], "facebook/bart-large-cnn")
if not os.path.exists(model_path):
    print("Downloading required models...")
    subprocess.call(["python", "download_models.py"])  # Download models if they aren't available

# Import your main GUI class here after setting up the environment
from gui import BasicApp

def main():
    app = BasicApp()
    app.mainloop()

if __name__ == "__main__":
    main()