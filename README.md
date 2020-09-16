# Python HTTP Server for web development!

**Disclaimer**:
Once you start the server, an instance of Chrome will open up. Due to limitations of the Selenium package, you will have to manually type in the address of the server. But after that you shouldn't encounter any issues!

## Description
An easy-to-use Local HTTP Server written in Python using the Socket and Selenium packages!

## Features
* Easy to use and fast to set up
* It detects file changes and conveniently refreshes your Chrome tab for you (Support for other browsers coming soon!)
* Supports all basic HTTP request methods (GET and POST)
* After following the instructions in SETUP.md, you will be able to start up a server in any directory just by typing `server.py` in your terminal!


## Installation & Requirements
#### Requirements:
* Python 3.x, you can install by visiting http://www.python.org
* Selenium python package
* Watchdog python package (it helps with watching for file changes in the directory of choice)
* Socket python package

**You can install all of them using `python -m install requirements.txt`**

#### Installation
**Check out SETUP.md to find out how to make this server available system-wide!**

## Usage
Open a command prompt in the directory in which you have the files and type `server.py`. You're done! You can now start editing your files for your website inside of the `web` directory and the server will display them at `http://127.0.0.1:8000`!