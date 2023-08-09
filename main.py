# main.py
from voice_recognition import VoiceRecognition
from unitycontroller import unitycontroller
from pynode import NodeMCUController

# Create instances of VoiceRecognition,NodeMCUController and UnityController
voice_recognition = VoiceRecognition()
unitconection = unitycontroller()



# Execute
voice_recognition.recognize()
unitconection.ConnectToUnity()
