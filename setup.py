from setuptools import setup, find_packages
import os


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name = 'sai-server',
    version = '0.1.0',
    description= 'Easiest way to develop websites locally!',
    url="https://github.com/erick-dsnk/sai-http-server",
    author = 'erick-dsnk',
    author_email = 'erick.8bld@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    scripts=[os.path.join(os.path.abspath(os.getcwd()), 'src', 'server.py')],
    install_requires = [
        'Click',
        'watchdog',
        'selenium',
    ],
    package_dir={'': 'src'},
    entry_points = 
    '''
        [console_scripts]
        sai=server:cli
    ''',
    classifiers=[
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent"
    ]
)