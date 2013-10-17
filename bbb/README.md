BeagleBone Black
================

SD card setup:
--------------

We use the Ubuntu Raring 13.04 image from [this site](http://www.armhf.com/index.php/download/)

```
cd /tmp
wget http://s3.armhf.com/debian/raring/bone/ubuntu-raring-13.04-armhf-rootfs-3.8.13-bone20.img.xz
xz -cd ubuntu-raring-13.04-armhf-3.8.13-bone20.img.xz > /dev/*YOURDEVICE*
```
ATTENTION: ne vous trompez pas de device!

C'est possible que `sudo su -` soit necessaire pour la derniere commande.

First Boot:
-----------

1. Figure out the IP address of the device. On the JDG-Machine network, goto http://192.168.1.1/ and look for computer named "ubuntu-armhf".
2. Boot the device; you should be able to connect to SSH with username *ubuntu* & password *ubuntu*
3. Do the "Ubuntu Setup" procedure below (only once).

Ubuntu Setup:
-------------

1. Go to `/etc/network/interfaces` and uncomment the wlan0 lines at the bottom. Setup the wifi name (JDG-Machine) and password.
2. Download the Machine 2014 repo: `git clone https://github.com/JDGETS/machine2014.git`
3. $ cd machine2014/bbb
4. $ make install-deps
5. $ install vim and screen from apt-get : sudo apt-get install screen vim
6. copy .bashrc and .screenrc from the scripts folder to the home directory
7. copy the .ssh folder to the home directory
8. copy interfaces file from the script folder to /etc/network/



