You can watch this project in action here : https://youtu.be/w_icYcQmUQk

I have completed an exciting project using Unity, Python, and IOT called AugmentedRealityHomeAssistant. The primary language utilized in this project is Python, and I have found a way to communicate through sockets. I also incorporated AR technology with the Vuforia plugin to track an image target and position 3D objects. 

To create the animation, I used Blender. I created a character controller script in Unity and used its animator to implement the logic for the animations.

In the Python script, there are four different scripts, each with a unique task, which includes voice recognition, communication with IOT devices, communication with Unity, and responding to recognized commands. 

Currently, I am working on developing an AI for this project, and I am attempting to train a model to respond like a human being.

I am happy to share this project and will be posting it on GitHub. I will provide a link once it is uploaded, and anyone can contribute, especially in the AI model part. Thank you!

Here is a step-by-step guide to execute this project:

1. Install Unity: https://unity.com/download
2. Create an empty 3D scene in Unity.
3. Create an account on Vuforia: https://developer.vuforia.com/
4. Create a license manager for your Unity project.
5. Create a target manager, which involves deciding what image to use as an image target in Unity. After creating the target manager, download it.
6. Download the Vuforia plugin for Unity: https://developer.vuforia.com/downloads/sdk.
7. Add the Vuforia SDK to your project.
8. Install the Vuforia AR camera. Before adding the AR camera, make sure to delete the main camera in the scene.
9. In the configuration, add your Vuforia license manager.
10. Select the image target and select the type from the database. Add your downloaded database here, making sure to add it to your project.
11. You are now all set to test your AR app. Anything above the target image will show after tracking the image in real-time.

Now, create an event system on the animator. You can create any amount of events with your animated 3D model and use layers to separate head movement and body. After that, add the animationcontroller.cs script to your character. You can modify it as you desire.

After finishing those steps, make sure you have installed Python on your PC. If not, download and install Python: https://www.python.org/downloads/. You also need a proper editor for Python; I am using Pycharm Community Version: https://www.jetbrains.com/pycharm/download/?section=window.

Now, download the project file "python_c#communication." After downloading it, open it using Pycharm, then edit this: 
home = C:\ProgramData\anaconda3 
implementation = CPython 
version_info = 3.10.5.final.0 
virtualenv = 20.13.0 
include-system-site-packages = false 
base-prefix = C:\ProgramData\anaconda3 
base-exec-prefix = C:\ProgramData\anaconda3 
base-executable = C:\ProgramData\anaconda3\python.exe 

In the pyvenv.cfg file, change the Home path to your Python.exe home folder. 

After that, activate the virtual environment by clicking on activate.bat in your script folder. 

Now, you can install all the necessary libraries. After doing that, you can implement IOT devices. In this project, I am using NodeMCU. To write for NodeMCU, download the Arduino IDE, and configure it for the NodeMCU board. To configure it, open the IDE and go to file, then select preference. In the additional board manager URL, paste this URL: http://arduino.esp8266.com/stable/package_esp8266com_index.json. After that, in the board manager, you can search for NodeMCU and install esp8266. 

Finally, plug in a NodeMCU board and flush the board with the SmartSwitch sketch.  

You can now utilize Unity and Python to control your NodeMCU with voice inputs and have your own personal AR assistant. Simply run Unity and then Python main to get started.
