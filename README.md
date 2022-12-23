# 410Project

# Project objective:
Peer-to-peer communication system using an IOT device to exchange information about the presence of an object and whether a collision has occured with this object. IOT device will "notify" or "ping" a user about both instances. Driving software developed in Java, along with the help of the @sign libraries and API.

# Hardware equipment requirements: 
Below is the list of required hardware components needed for this project. It is essential to set up the equipment properly. The resistors and LED lights serve for debugging purposes and thus the project device will work without them.
The list below is given in the order of `name of part` and `count` as follows:

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
11. `Micro USB cable (able to exchange data)`, `1`

# Software requirements: 

OS: From Windows 7 upto Windows 10, macOS 10.15 (Catalina) to 13 (Ventura), or any Linux LTS operating system (preferably Ubuntu)
Suggested code editors or IDEs to use:
1. Microsoft Visual Studio Code(Overall good). Extensions that came in handy are: `Pico-W-Go`, `PlatformIO IDE`

2. Android Studio Dolphin (For application development in Flutter/Dart).

3. JetBrain IntelliJ(for Java) and Pycharm(for Python).

> If you intend to develop in Java:
Any version of Java JDK LTS from version 8.0 to 17.0 will be needed to compile and run "Application.java" file. This program is found in this root directory. Maven is also required for this project, as it is used to recieve data from the server that the Pico W device sends to.

> If you intend to develop in Python and Micro Python:
The latest version of Python and Python 3 should do just fine. Micro Python is needed in order to code the Pico. `Pico-W-Go` extension for Microsoft Visual Studio Code is great for connecting and uploading code to the device. If code from Arduino is understood it can be simple to translate to Micro Python.

> If you intend to develop a mobile application using Flutter and Dart:
Use the latest version of the Flutter SDK. Check out this [link](https://docs.flutter.dev/get-started/install) for a step by step guide on how to properly set up the SDK. The latest version of the Dart SDK should also be installed. [Here](https://dart.dev/get-dart) is a guide on how to setup Dart.

# Insights for the project
Part of the goal of our project was to make use of the @sign libraries and API as a part of professor Kenneth Fletcher's (@kkfletch) course CS410. Our group was enrolled in his course in the Fall 2022 semester at University of Massachusettes Boston.

In our project, we were to make use of the @sign API and libraries in order to develop and contruct a working device capable of securely transferring information over the internet. The libraries used intensively were the AtClient, AtSign, KeyBuilders, Keys, Keys.PublicKeys. All these libraries, along with a whole lot more can be found on the @sign foundation github repository [here](https://github.com/atsign-foundation/)

Depending on which programming language you choose to use, @sign has you covered with how to get yourself familiar with their modules and libraries.
Step-by-step instructions on properly setting up the software environment can be found in this [link](https://docs.atsign.com/), published by @sign themselves. Feel free to check it out.

# Project Details:
"Sense for a collision and send the data between two atSigns.
One atSign will be the device and the other atSign will 
be displaying the data on an application."

The purpose of this project is to demonstrate secure communication between two devices or two "involved parties", over the internet with the help of `@signs`. These `@signs` are the creation of the company called "@sign", which allows their users to create and own an unique individual identity on the company servers. Think of it like an email address or an online gamertag, which is distinct for every user. Using an `@sign` will allow the users to communicate with each other through the @sign company servers while maintaining absolute privacy. This privacy is provided due to the @sign company's encryption protocol for data transmission, as the data is encrypted using special public and private keys, and it is the keys that are shared among `@signs`. Once a key is recognized by the @sign servers, the data is then sent out to that @sign. This means no sudden advertisements about something which you have been talking about in your group chats.

That being said, "communication" between `@signs` is not limited to just text chats or voice calls. These `@signs` are capable of being installed on `IOT` devices, allowing the devices to send and receive encrypted data over the internet. `IOT` stands for `Internet Of Things`, where a device is built using
a combination of sensors that only serves to send and receive certain forms(s) of data while connected to the internet. Other than the listed parts mentioned above, there is a large variety of sensors available for anyone to purchase and start builing their own IOT device. Example uses of `IOT` devices include how a hospital nurse can be paged directly from the front desk, and a doctor directly receiving heart-rate data from a patient using an `IOT` device to measure the heart-rate etc. 

> Starter IOT kits are available for purchase on Amazon and can also be found at MicroCenter and some hardware stores. 

For this project, we have joined together and developed an `@sign IOT` device. The objective of this project was that our device needs to be 
capable of sensing the presence of an object or "obstacle" in it's vicinity. Furthermore, our device should also be able to detect when a collision has
occured with "obstacle".

The two devices (or people behind the scene) are one in possession of the Pico W device and another person on a windows or mac or linux based computer running the "Application.java" program. Both need to be connected to the internet for this project to work. The Pico W device will send a "message" to this computer about the obstacle and collision detection through the onboarded `@sign`.

# Potential use case

Due to it's small size and scale, along with it being very light weight, our project IOT device can be installed and embedded onto remote controllable devices, such as drones and robots. This will allow the controller, or even the drone or robot, to know about collisions and avoid potentially damaging the operational device. Thus, this can be installed on drones and be sent out for exploration, it can be attached onto robot body parts as to prevent potentially damaging it's hardware components. Maybe sometime it'll be used on robots sent outfor interplanetary explorations, but for now we can stick to Earth.

# How to Set up the Device
We recieved the resistors, LEDS, jumper cables (wires), 2 Infrared Obstacle Avoidance sensors, 2 Knock sensor Modules, 1 Passive Buzzer Module, 1 Active Buzzer Module and 2 Collision Sensors. We also recieved a breadboard and the Raspberry Pi Pico. We wanted to put all the sensors together so I (Ronaldo) got another breadboard and more wires so that all the sensors could be connected to the pico. I (Ronaldo) used to be a Computer Engineering major so I had those parts laying around. If you, any one reading this, wants to connect all sensors you will need another breadboard and more wires. 

To Begin setting up:

<img src="https://cdn-shop.adafruit.com/970x728/4883-06.jpg" width=50% height=50%>

Image [Source](https://www.adafruit.com/product/4883?gclid=CjwKCAiAnZCdBhBmEiwA8nDQxSzivf3NmQMk7iUWZptxnislaWqZFTsSv0emR_lxNcoU3eRMLAi6whoCJeYQAvD_BwE)

The image above is a raspberry pi pico. We can see the pins for it are not connected. Unfortunately that means it needs to be soldered. It is not the easiest thing to do. If anyone can find a way to get the pins on the pico working without soldering be my guest. I (Ronaldo) have found it hard to get devices like the pico to work properly without soldering. I knew someone who knew how to solder and they soldered the board for us. Next step is to put it on our breadboard.

<img src="https://www.allelectronics.com/mas_assets/cache/image/3/3/a/1/13217.Jpg" width=40% height=40%>

Image [Source](https://www.allelectronics.com/item/pb-400/solderless-breadboard-400-contacts/1.html)

The breadboard is shown above. The pico perfectly fits in the middle from the letters cde and fgh. The pico has 40 pins to we goes into the holes up to the number 20. 
We also need to mention how the breadboard works. The numbers are the rows and the rows are connected horizontally. For example row 1 A is connected up to row 1 E. Row 1 A is not connected to row 2 A. If you put a wire between those then they would be connected. Another thing to mention is the rails on the side with the + and -. The + denotes a voltage in and the red line means that all those holes are connected. The - denotes ground and the blue line mean all the holes next to it are all connected. These rails are very useful because they provide easy access of voltage in and ground. Now we need to start connecting all the sensors.

The resistors and LEDS that were provided were to be used for debugging. We did not use them at all. Just letting you know that if you needed to use the LEDs you would need the resistor otherwise the LED would burn out. The buzzer that was given to us was a good debugger. 

We should first discuss how these connections will happen.

<img src="https://cdn-shop.adafruit.com/970x728/4883-06.png" width=60% height=60%>

Image [Source](https://www.adafruit.com/product/4883?gclid=CjwKCAiAnZCdBhBmEiwA8nDQxSzivf3NmQMk7iUWZptxnislaWqZFTsSv0emR_lxNcoU3eRMLAi6whoCJeYQAvD_BwE)

This shows how the pico is set up. It looks complicated but it is not. The GP pins are basically the ones we use. There is more specific things about each pins but we do not need to worry about the details. We have 4 components so lets just use 4 pins. We can use GP0 to GP3. We should use the VBUS pin as well because the contains the voltage for each component. We should also use GND which is ground so that we can ground the components. Any GND should be fine. We plug in wires in the breadboard row associated with those pins. 

So first let us start with the ir sensor (Infrared Obstacle Avoidance sensors).

<img src="https://arduinomodules.info/wp-content/uploads/Arduino_KY-032_IR_obstacle_avoidance_sensor_connection_diagram-1024x668.png" width=50% height=50%>

Image [Source](https://arduinomodules.info/ky-032-infrared-obstacle-avoidance-sensor-module/)

This is the setup with arduino using the same sensor we have but it is easy to follow. The red wire is the voltage in so you connect it to the pin that voltage. You can connect it to the rail which you should have connected with the wire connected to the VBUS pin on the pico. The black wire is ground. The blue wire is one of the GP pins. We can connect it to any GP pin. We do not need to worry about the 4th pin. Do not plug anything into it.

Now the Crash Sensor.

<img src="https://wiki.keyestudio.com/images/thumb/f/f3/Ks0021.png/700px-Ks0021.png" width=50% height=50%>

Image [Source](https://wiki.keyestudio.com/Ks0021_keyestudio_Collision_Sensor)

Again this has 3 pins. 1 is the voltage in and the other in ground. The last pin again will be connected to a GP pin.

Now the Buzzer.

<img src="https://wiki.keyestudio.com/images/thumb/1/18/Ks0018-.png/600px-Ks0018-.png" width=50% height=50%>

Image [Source](https://wiki.keyestudio.com/Ks0018_keyestudio_Digital_Buzzer_Module)

Again this has 3 pins. 1 is the voltage in and the other in ground. The last pin again will be connected to a GP pin.

Lastly the Knock Sensor.

<img src="https://wiki.keyestudio.com/images/thumb/7/75/Ks0024-.png/700px-Ks0024-.png" width=50% height=50%>

Image [Source](https://wiki.keyestudio.com/Ks0024_keyestudio_Knock_Sensor_Module)

Once again this has 3 pins. 1 is the voltage in and the other in ground. The last pin again will be connected to a GP pin.

Again, all those voltage in and grounds can be connected to the rails and the rest are connected to the GP pins on the pico.



# Pre-requisites before running:
* Ensure that you are upto date on your windows/mac/linux operating system.
* Make sure that your internet connection is stable. Try watching `ONE` YouTube shorts video.
* If you wish to run our version of the project as it is, all you need to do is have Java JDK. Ensure that your Java Jdk library are properly installed and upto date, try to make a "Hello World!" program and feel like a god tier coder! jk. Also, you do not need to worry onboarding/uploading any @signs becasue we just left our ones in the code. 
* If you are intending to write your own fucntional code or application in Python or Flutter/Dart, make sure to clone the @sign library for those languages and properly import them into your application file. Python/MicroPython libraries can be found @ [this](https://github.com/atsign-foundation/at_pico_w), while for Flutter/Dart look @ [here](https://github.com/atsign-foundation/at_client_sdk). [see what I did there >_<]

# What to do and what to expect for the project
> Two operational computer systems, any OS is fine, are needed.

> On one computer, we need to verify stable internet connection.

> Make sure that your firewall allows the device to access the internet through the connected computer.

> After the device has been set up properly, it has to be connected to the computer. We need to make sure we have a micro usb cable that is able to transfer data.

> It is now time to create @signs for yourself and the Pico W device. Simply go to @sign's website by clicking [here](https://my.atsign.com/login). Details about creating @signs are provided in the website.

> Depending on which code editor you use, you first upload the code found in "CrashData Send" on the Pico W device. This is easiest with `Pico-W-Go` as you can simply just click upload project and it uploads to the pico.

> After that is complete, you are to run the "Application.java" file found in the root directory of this repository. This java file will display a GUI. It allows us to choose which sensor data we want to see. Since we can only see the ir obstacle sensor and the crash sensor we will see data from those.

> With a stable internet connection and an @sign onboarded onto the Pico W device, the device will now be able to send out data when it will detect an object in its proximity and also send a message when a collision has taken place. In the GUI when we choose which data we want to see, each one shows different results. Obstacle detection will count how many seconds we see the object. Crash detection will count how times the crash sensor was hit. It will save that value even when we change the mode.

# Contents in each directory
## More details can be found in each directory

### .idea
Config logs generated by VS code when compiling and running the Application.java program

### CrashData receive
Code written in java that recieves the data from the pico which was sent in the python file in CrashDataSend. This also contains or App to display the data in a GUI.

### CrashDataSend
Back-end program which allows data, in our case is information about a crash, to be sent through the @sign servers between @signs

### PythonTestFiles
Code for debugging and testing of the components used in the project. 

### SendDataTest
Java code to test the functionality of the Pico W when it comes to receiving data from the @sign servers

### Ignore all this
Please just go along with the name. It's a collection of the failed attempts in creating a flutter/dart application based @sign API
for our project. It also contained the clones of "atmosphere_pro", found [here](https://github.com/atsign-foundation/atmosphere_pro)
and "atmosphere", found [here](https://github.com/atsign-foundation/atmosphere) repositories. There repositories were mainly clones
to be looked at how the @sign API was implemented and used in the creation of mobile applications. 

# That is all, thank you!
