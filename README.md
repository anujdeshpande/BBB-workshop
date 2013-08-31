BBB-workshop
============

Demos for a Hands on BeagleBone Black workshop
-------------------------------------------------------------------------------

* To have network access on the Black using just the USB wire, follow these steps.
  On the Black do:

        # /sbin/route add default gw 192.168.7.1
		# echo "nameserver 8.8.8.8" >> /etc/resolv.conf

  On the Linux host from which you want to route:

        # sudo iptables -A POSTROUTING -t nat -j MASQUERADE
        # sudo echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward > /dev/null

  Now on the BBB:
  
        # ping google.com
  Have tested this on Angstrom, but should work on Ubuntu, etc. too.

* Transferring files in between host machine and BeagleBone Black

		# sftp root@192.168.7.2
Common used commands with ftp are mput, mget, exit. You can also use cd and ls to move through remote filesystem.
Another similar command is scp which is handy if you want to transfer files by in a script.
* BeagleBone Black and OpenCV
  Derek Molloy's sample code is in boneCV.cpp. To compile use:

		# g++ -O2 `pkg-config --cflags --libs opencv` boneCV.cpp -o boneCV
  OpenCV 2.4.2 comes preinstalled with the Angstrom image.
  Current version of the Angstrom doesn't have python-opencv package by default. To install use:

		# opkg install http://dominion.thruhere.net/koen/angstrom/python-opencv_2.4.2-r3.10_armv7a-vfp-neon.ipk

Arduino-like code on the Black
-------------------------------------------------------------------------------

* Setting up Userspace Arduino

		# git clone http://github.com/prpplague/Userspace-Arduino.git
		# cd Userspace-Arduino/arduino-makefile/examples
* To compile any of the examples, cd to the directory

        # make
		# cd 
Python on the Black
-------------------------------------------------------------------------------
* Setup network access
* Get pip
  
		# opkg update
		# opkg install python-pip
* To install flask

		# pip install https://pypi.python.org/packages/source/F/Flask/Flask-0.10.1.tar.gz#md5=378670fe456957eb3c27ddaef60b2b24
		
* Setting up Adafruit_BBIO

		# git clone git://github.com/adafruit/adafruit-beaglebone-io-python.git
		# opkg update && opkg install python-distutils python-smbus
		# cd adafruit-beaglebone-io-python
		# python setup.py install



Links for more information about above demos
-------------------------------------------------------------------------------

* [Derek Molloy's opencv tutorial](http://derekmolloy.ie/beaglebone/beaglebone-video-capture-and-image-processing-on-embedded-linux-using-opencv)
* [Userspace Arduino wiki](http://elinux.org/Userspace_Arduino)
* [Adafruit BBIO](http://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/using-the-bbio-library)


Links for information about BeagleBone Black in general
-------------------------------------------------------------------------------
If you are stuck someplace, your first port of call ought to be the mailing list archives( high chances that someone has faced that problem before).
If that doesn't yield anything, you can surely find help on the IRC channel.

* [Mailing list: Google Group](https://groups.google.com/forum/?fromgroups#!forum/beagleboard)
* IRC Channel #beagle on Freenode : *VERY* active and helpful.
* List of available [capes](http://circuitco.com/support/index.php?title=BeagleBone_Capes)
* [Google+ Community Page](https://plus.google.com/communities/104960311812236799231)
* List of [projects](http://beagleboard.org/project) done with Beagle*
