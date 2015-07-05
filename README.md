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
===============

#### If you're interested in contributing into this library

- This code is all written in Python, and it is possible to be written in other programming languages to support Yee Light Blue into other languages as well. **Credits to Yap Wen Jiun for reverse engineering the Yee Light Blue**

- The class of the Yee Light Blue is placed inside the yeelightblue.py in which contains 10 methods or functions to control the Yee Light Blue.
