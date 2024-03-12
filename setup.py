import os

from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), "README.md"), "r").read()

setup(
    name='example_package_saketc',
    version='0.0.3',
    packages=find_packages(),
    long_description=README,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        "console_scripts": ["hello = example_package_saketc.example:hello"]
    },
)
