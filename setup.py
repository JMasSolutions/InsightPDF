# setup.py

from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class CustomInstallCommand(install):
    """Customized install command to run post-install scripts."""

    def run(self):
        # Run the standard install process
        install.run(self)
        # Run the model download script after installation
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
        "numpy<2",
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
    cmdclass={
        'install': CustomInstallCommand,  # Run the custom install command
    },
)