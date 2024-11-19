import spacy
import subprocess
import sys

def download_spacy_model():
    try:
        # Check if the model is already installed
        spacy.load("en_core_web_sm")
    except OSError:
        print("Spacy model 'en_core_web_sm' not found. Downloading it now...")
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
        print("Download complete.")

