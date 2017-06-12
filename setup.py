import os
from setuptools import setup

DEPENDENCY_LINKS = [
    "-e git+https://github.com/cormac-yobota/pytest-demo-parent.git@0.1.0#egg=pytest-demo-parent"
]
INSTALL_REQUIRES = [
    "pytest-demo-parent==0.1.0",
]
VERSION="0.1.0"

setup(
    version=VERSION,
    dependency_links=DEPENDENCY_LINKS,
    install_requires=INSTALL_REQUIRES, 
    name = "pytest-demo-child",
    url = "http://packages.python.org/an_example_pypi_project"
)

