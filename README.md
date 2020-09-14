# Python HTTP Server for web development!

**Disclaimer**:
Once you start the server, an instance of Chrome will open up. Due to limitations of the Selenium package, you will have to manually type in the address of the server. But after that you shouldn't encounter any issues!

## Description
An easy-to-use Local HTTP Server written in Python using the Socket and Selenium packages!

## Features
* Easy to use and fast to set up
* It detects file changes and conveniently refreshes your Chrome tab for you (Support for other browsers coming soon!)
* Supports GET requests and POST requests are coming soon as well

## Installation & Requirements
#### Requirements:
* Python 3.x, you can install by visiting http://www.python.org
* Selenium python package, install using pip (Python's package manager): `pip install selenium`
* Watchdog python package (it helps with watching for file changes in the `web` directory), install with: `pip install selenium` 
* Socket python package, install with: `pip install socket`


## Usage
Open a command prompt in the directory in which you have the files and type `python server.py`. You're done! You can now start editing your files for your website inside of the `web` directory and the server will display them at `http://127.0.0.1:8000`!