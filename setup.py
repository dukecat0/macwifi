from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="macwifi",
    version="0.0.3",
    author="meowmeowcat",
    author_email="",
    description="Macwifi is a Python module that helps you to manage the WiFi on macOS.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meowmeowmeowcat/macwifi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS"
    ],
    packages=["macwifi"],
    python_requires=">=3.6",

)
    