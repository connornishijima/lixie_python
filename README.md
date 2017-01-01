# Lixie-Python

Python module for driving Lixie Displays!

# Installation

Before installing, connect your first Lixie like this:

![Wiring diagram](http://i.imgur.com/PyvOyog.png)

I've done my best to make this extremely easy - just enter the following one-liner into a Raspberry Pi command line:

    sudo wget https://raw.githubusercontent.com/connornishijima/lixie_python/master/lixie_installer.py && sudo python lixie_installer.py
    
The fetches the installer script from this repository and starts it. You'll see a screen like this:

    888      8888888 Y88b   d88P 8888888 8888888888
    888        888    Y88b d88P    888   888
    888        888     Y88o88P     888   888
    888        888      Y888P      888   8888888
    888        888      d888b      888   888
    888        888     d88888b     888   888
    888        888    d88P Y88b    888   888
    88888888 8888888 d88P   Y88b 8888888 8888888888
    ----------- PYTHON LIBRARY INSTALLER ----------

    This script will take care of installing
    Lixie and all of its dependencies.
    Ready to go? (y/n)

Confirm you're ready to start, and the installer will take care of all fetching, compiling, and dependencies. This make take up to 30 minutes if your Raspbian is out of date. Upon finishing, the script will self-import the new library and display a counting animation on your displays!
