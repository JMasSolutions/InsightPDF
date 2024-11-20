import spacy
import subprocess
import sys

from env.config import SPACY_MODEL

def download_spacy_model(model_name=SPACY_MODEL):
    try:
        spacy.load(model_name)
    except OSError:
        print(f"Spacy model '{model_name}' not found. Downloading it now...")
        subprocess.check_call([sys.executable, "-m", "spacy", "download", model_name])
        print("Download complete.")

download_spacy_model()
