# 410Project

# Project objective:
Peer-to-peer communication system to exchange information about
the presence of an object and whether a collision has occured
with this object. Driving software developed with the help of
java libraries and API along with the help of the @sign foundation and API.

# Hardware equipment requirements: 
Below is the list of required hardware components needed for this project.
It is essential to set up the equipment properly. The resistors and LED lights
serve for debugging purposes and thus the device will work without them.
The list below is given in the order of: `name of part` and `count`.

1.  `Raspberry Pi Pico W`, `1`
2.  `Pico Headers`, `1`
3.  `Solderless Breadboards (ALT)`, `1`      
4.  `PCs Jumper Wires`, `10`
5.  `Resistors`, `10`
6.  `(1, 8) Active Buzzer Module`, `1`
7.  `(1, 16)` `Collision Sensor`, `2`
8.  `(1, 9) Passive Buzzer Module`, `1`
9.  `(2, 35) Infrared Obstacle Avoidance`, `2`    
10. `(1, 7) Knock sensor Module`, `2`	

# Software requirements: 

OS: From Windows 7 upto Windows 10, macOS 10.15 (Catalina) to 13 (Ventura), or any Linux LTS operating system
Suggested code editors or IDEs to use:
1. Microsoft Visual Studio Code.
Extensions that came in handy are: `Pico-W-Go`, `PlatformIO IDE`
2. Android Studio Dolphin.
3. JetBrain IntelliJ(for Java) and Pycharm(for Python).

> If you intend to use Java:
Any version of Java JDK LTS from version 8.0 to 17.0

> If you intend to use Python:
The latest version of Python and Python 3 should be alright.

> For flutter/dart
Use the latest version of the flutter SDK. Check out this [link](https://docs.flutter.dev/get-started/install)
for a step by step guide on how to properly set up the SDK.
The latest version of the Dart SDK should be used. [Here](https://dart.dev/get-dart) is a guide on how to setup Dart.

Since the goal of our project was to make use of the @sign libraries and API
The libraries from the @sign website and github repository. Specifically for this project we made use of the 
AtClient, AtSign, KeyBuilders, Keys, Keys.PublicKeys.
All these, and a whole lot more can be found on the @sign github repository [here](https://github.com/atsign-foundation/)

# Project Details:
"Sense for a collision and send the data between two atSigns.
One atSign will be the device and the other atSign will 
be displaying the data on an application."
This project is to demonstrate secure communication between two devices over the internet with the help of "@signs".
@signs are the creation of the company called @sign, which allows their users to own a unique identity on their server.
Think of it like an email address. Using an @sign will allow the users to communicate with each other through 
the @sign company servers while having absolute privacy. This means no sudden advertisements about something 
which you have been talking about in your friends chats. That being said, "communication" between @signs
is not limited to just text chat or voice calls. These @signs are capable of being installed on IOT devices,
which allows the devices to receive encrypted data. `IOT` stands for `Internet Of Things`, where a device is built using
a combination of sensors that only serves to send and receive a certain form of data. Other than the listed parts mentioned before,
there are a large variety of sensors available for anyone to purchase and start builing their own IOT device. 
Examples include how a hospital nurse can be paged about 
or a doctor receiving heart rate data from the patient etc, through an IOT device

......more on this later.....

The two devices (or people behind the scene) are the Pico W device and one windows or mac or linux device.
Both need to be connected to the internet for this project to work.
The Pico W device will send a "message" to another computer, with the help of an @sign,

# // insert how to set up device //
replace all in this header with the setup instructions
start from the very beginning, like the way we received
all the part individually
go over one component at a time, where to connecet, what to solder
we never ended up using the resistors and LEDs for debugging, upto
you if you want to mention those in here, it's cool if we dont ig

# Pre-requisits before running:
* Ensure that you are upto date on your windows/mac/linux operating system.
* Make sure that your internet connection is stable. Try watching `ONE` YouTube shorts video.
* Ensure that your Java jdk library are properly installed and upto date,
make a "Hey you ;)" program and be the god of coders! jk.
* Properly clone the @sign library for java. The repository is labelled "at_java"
and can be found @ this [link](https://github.com/atsign-foundation/at_java). [see what i did there >_<]

Two operational computer systems, any OS is fine, are needed.
On one computer, we need to verify stable internet connection.
Make sure that your firewall allows the device to access the internet
through the connected computer.


the "Application.java" file found in the 
root directory of this repository can be run t

# Contents in each directory
##### More details can be found in each directory

## .idea
Config logs generated by VS code when compiling and running the Application.java program

## CrashData receive
Driver code written in python that is to be installed on the Pico W device so that an @sign can be onboarded and used

## CrashDataSend
Back-end program which allows data, in our case is information about a crash, to be sent through the @sign servers between @signs

## PythonTestFiles
Code for debugging and testing of the components used in the project. 

## SendDataTest
Java code to test the functionality of the Pico W when it comes to receiving data from the @sign servers

## Ignore all this
Please just go along with the name. It's a collection of the failed attempts in creating a flutter/dart application based @sign API
for our project. It also contained the clones of "atmosphere_pro", found [here](https://github.com/atsign-foundation/atmosphere_pro)
and "atmosphere", found [here](https://github.com/atsign-foundation/atmosphere) repositories. There repositories were mainly clones
to be looked at how the @sign API was implemented and used in the creation of mobile applications. 

## maven
This was not supposed to be here.
