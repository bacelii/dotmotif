#!/usr/bin/env python3

import os
import io
from pathlib import Path
from setuptools import setup, find_packages, Command
from typing import List

def get_install_requires(filepath=None):
    if filepath is None:
        filepath = "./"
    """Returns requirements.txt parsed to a list"""
    fname = Path(filepath).parent / 'requirements.txt'
    targets = []
    if fname.exists():
        with open(fname, 'r') as f:
            targets = f.read().splitlines()
    return targets

def get_links():
    return [
        #"git+https://github.com/bacelii/machine_learning_tools.git"
    ]


"""
git tag {VERSION}
git push --tags
python setup.py sdist
twine upload dist/*
"""

VERSION = "0.9.2"

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

setup(
    name="dotmotif",
    version=VERSION,
    author="Jordan Matelsky",
    author_email="jordan.matelsky@jhuapl.edu",
    description=("Find graph motifs using simple, intuitive notation"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2.0",
    keywords=["graph", "motif"],
    url="https://github.com/aplbrain/dotmotif/tarball/" + VERSION,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    classifiers=[],
    install_requires=get_install_requires(), #external packages as dependencies
    dependency_links = get_links(),
    include_package_data=True,
)
