from setuptools import setup, find_packages

setup(
    name='HelloWorldCLI',
    version='0.0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        "console_scripts": ["hello = example_package_saketc.example:hello"]
    },
)
