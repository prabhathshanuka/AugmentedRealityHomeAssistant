import speech_recognition as sr
import time
from dialouges import Speach

class VoiceRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def recognize(self):

        while True:
            # Define the audio source (microphone)
            with sr.Microphone() as source:
                print("Listening...")
                audio = self.recognizer.listen(source, phrase_time_limit=10)  # Limit the listening time to 3 seconds

            try:
                # Recognize speech using the Sphinx engine for offline speech recognition
                recognized_text = self.recognizer.recognize_google(audio)
                print("Recognized Text:", recognized_text)
                Speach.process_command(recognized_text)

            except sr.UnknownValueError:
                print("Unable to recognize speech.")

            except sr.RequestError as e:
                print("Error:", str(e))
            # Wait for 1 second before listening again
            time.sleep(1)


