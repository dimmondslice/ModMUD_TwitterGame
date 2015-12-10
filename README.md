#TwitterGame

Prerequisites
----------------
- Python 2.7
 - https://www.python.org/download/releases/2.7/
 - Look for either the Windows x86 MSI Installer or Windows X86-64 MSI Installer depending upon your operating system.
- Pip 7.1.2
 - Installation instructions: https://pip.pypa.io/en/stable/installing/ 
 - This is not required for the other third-party applications, but it does make things significantly easier to install.
- Pillow
 - Installation instructions: http://pillow.readthedocs.org/en/3.0.x/installation.html 
 - If pip has successfully been installed, you can install pillow by running “pip install pillow” in the command line.
- TweePy
 - Installation instructions: http://docs.tweepy.org/en/v3.5.0/install.html 
 - If pip has successfully been installed, you can install tweepy by running “pip install tweepy” in the command line.

Installation and Start Up
-----------------------------
- Unzip the TwitterGame folder into the directory of your choice.
- Double-click gui.py to run the Host Client.

Game Setup
------------

- From the host client, press the **Set Output Account** button. This will open a web browser and ask you to authenticate a Twitter account of your choice that the bot will use to send and receive messages to and from the players.
- Once your account is authenticated, Twitter will provide a numeric code. Place this code into the box above the **Validate** button, then press the **Validate** button.
- Finally, add the Twitter handles of the players of your game into the Whitelist by typing them into the box (no @ before the name) and then hitting the **Add User** button.
- You can remove players from the Whitelist by clicking the username in the list and hitting the **Remove User** button.
- Once your players are all added, hit the **Start Game** button.