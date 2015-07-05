Yee-Light-Blue
==============

Writing library for yee light blue using python for raspberry pi

- Enabling Raspberry Pi to control Yee Light Blue freely.

Running test.py requires root

===============

### Some guidelines into using this library

#### Install all the pre-requisite libraries and third-party tools

*Credits to Ramin Sangesari in hackster.io for this*

**1. Get the required libraries**
```
sudo apt-get install libusb-dev libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev
```
**2. Download Bluez**
```
sudo mkdir bluez
cd bluez
sudo wget www.kernel.org/pub/linux/bluetooth/bluez-5.31.tar.xz
```
**3. Unzip and Compile Bluez**
```
sudo unxz bluez-5.31.tar.xz
sudo tar xvf bluez-5.31.tar
cd bluez-5.31
sudo ./configure --disable-systemd
sudo make
sudo make install
```

**4. Python Libraries**

`pip install pexpect`

OR:

`easy_install pexpect`

If these doesn't work for you, it is most likely that you're missing pip and easy_install. You can either install them or you can manually install pexpect.

######Manual Installation of pexpect
Go to https://pypi.python.org/pypi/pexpect/ and download the latest version.

For Linux System Only (Since I'm talking about Raspberry Pi here)
```
tar xzf pexpect-x.x.tar.gz
cd pexpect-x.x
sudo python ./setup.py install
```

===============

#### If you're interested in contributing into this library

- This code is all written in Python, and it is possible to be written in other programming languages to support Yee Light Blue into other languages as well. **Credits to Yap Wen Jiun for reverse engineering the Yee Light Blue**

- The class of the Yee Light Blue is placed inside the yeelightblue.py in which contains 10 methods or functions to control the Yee Light Blue.

`__init__: contructor function, receives `

#### TODO
- Finish up the discover function/method
-- Inside this method, using *sudo hcitool lescan* we can scan and get the MAC address of the Yee Light Blue and filtering that we would be able to discover the Yee Light Blue

- There's a few more UUID/Handles that the Yee Light Blue has for example flickering and auto delay timer, however, with the current functionality you are most likely able to perform basic and cool things. You're more than welcome to complete it.
