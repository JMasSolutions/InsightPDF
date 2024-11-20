import os
import subprocess

# Check if models are downloaded
if not os.path.exists(os.path.expanduser("~/.cache/huggingface/transformers/facebook/bart-large-cnn")):
    print("Downloading required models...")
    subprocess.call(["python", "download_models.py"])

from gui import BasicApp  # Import your main GUI class here

def main():
    app = BasicApp()
    app.mainloop()

if __name__ == "__main__":
    main()