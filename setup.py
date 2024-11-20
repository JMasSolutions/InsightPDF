from setuptools import setup, find_packages
import subprocess

# Function to run the model download script after installation
def post_install():
    print("Running model downloads...")
    subprocess.call(["python", "download_models.py"])

setup(
    name="InsightPDF",
    version="1.0.0",
    author="Joan Mas Castella",
    description="A PDF summarizer and Q&A application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pdfplumber",
        "spacy",
        "transformers",
        "torch",
        "customtkinter",
    ],
    entry_points={
        "console_scripts": [
            "insightpdf=main:main",  # Assumes `main` is the entry function in main.py
        ],
    },
    include_package_data=True,
    data_files=[("", ["requirements.txt"])],
    cmdclass={
        'install': post_install,  # Runs post-install function to download models
    },
)