"""Setup script for realpython-reader"""

import os.path
from setuptools import setup


#The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

#the text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="prasad-reader",
    version = "1.1.0",
    description = "Read the latest real python tutorial",
    long_description = README,
    long_description_content_type = "text/markdown",
    url = "https://github.com/realpython/reader",
    author = "Prasad",
    author_email = "info@realpython.com",
    license = "MIT",
    classifiers = [
         "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    packages = ["reader"],
    include_package_data = False,
    install_requires = [
        "feedparser", "html2text", "importlib_resources", "typing"
    ],
    entry_points = {"console_scripts": ["realpython=reader.__main__:main"]}

)