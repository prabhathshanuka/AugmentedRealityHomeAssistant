# AugmentedRealityHomeAssistant
I am excited to share my latest project involving Unity, Python, and IOT.
The primary language used in this project is Python, and I have devised a way to communicate through sockets.
Additionally, I utilized AR technology with the help of Vuforia plugin to track an image target and position 3D objects.

For the animation part, I used Blender.
In Unity, I created a character controller script and used its animator to implement the logic for animations.

In the Python script, there are four different scripts, each with a unique task. These scripts include
voice recognition,
communication with IOT devices,
communication with Unity, and
responding to recognized commands.

I am currently working on developing an AI for this project. and am attempting to train a model to respond like a human being.

I am pleased to share this project and am willing to post it on GitHub. I will provide a link once it is uploaded, and anyone can contribute, especially in the AI model part.
Thank you!

This is  a step by step guide to execute this project:
first you have to install unity: https://unity.com/download
affter that you can create a empty 3d scene in unity
go to vuforia and make an account: https://developer.vuforia.com/
after create an acount youo have te create licen manager for your unity project
then after you have to make target manager: in here you have to decide what image you will use as a image target in unity. you have do download you created target manager.
affter adding those  download vuforia plugging for unity: https://developer.vuforia.com/downloads/sdk
after download sdk you have to add it to your project.
affter install vuforia sdk you can add vuforia AR camera before adding ar camera you make sure to delete main camera in the scene.
affter adding ar camera in the configeration you have to add your vuforia licen manager 
then select image target in there select type from database then you have to add your downloaded database in here: make sure you add that database in to your project
now you all set to test your ar app.
add anything above on target image will show after track that image in real time. 

now you have to create event system on animator:
    you can create any amount of event with your animated 3d model use layers to separatehead movement and body
after that you have to add animationcontroller.cs script to your character. you can modify as you want

after finish those step now you have to make sure you have install python in your PC:if not download and install python: https://www.python.org/downloads/

after installed pyhton you have to make sure you have proper editor for python in here i am using pycharm comunity version: https://www.jetbrains.com/pycharm/download/?section=window

now you have to download project file "python_c#communication" after download that open it using pycharm then you have to edit this:
home = C:\ProgramData\anaconda3
implementation = CPython
version_info = 3.10.5.final.0
virtualenv = 20.13.0
include-system-site-packages = false
base-prefix = C:\ProgramData\anaconda3
base-exec-prefix = C:\ProgramData\anaconda3
base-executable = C:\ProgramData\anaconda3\python.exe

in pyvenv.cfg file change Home path to your pythone.exe home folder

after that you have to activate virtual envirement click activate.bat in your script folder 

now you can install all the necesary libraries

affter doing that you can impliment iot device in here i am using nodemcu
to writ for node mce u want 
  



