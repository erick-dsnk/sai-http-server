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
* Chrome webdriver (Selenium is based on the chromedriver for refreshing your tab.), visit https://chromedriver.chromium.org/home


#### Chrome Webdriver installation
1. Visit https://chromedriver.chromium.org/home and download the latest stable release of the driver
2. Once you downloaded it, go to your C:/ drive and create a folder called `webdrivers` and copy the chrome webdriver to that folder.
3. Open the Windows menu by pressing the Windows key and type 'Environment Variables', a settings result should appear. Open it, then go to Environment Variables, then scroll down to where it says 'Path', select it then click 'Edit', create a new entry and enter the path to the folder you created earlier. If you followed the steps it should be `C:\webdrivers`.
4. You're done! You can now run the server with no problem.

## Usage
Open a command prompt in the directory in which you have the files and type `python server.py`. You're done! You can now start editing your files for your website inside of the `web` directory and the server will display them at `http://127.0.0.1:8000`!