import json
import requests
import pyttsx3
import pyaudio
from vosk import Model, KaldiRecognizer



engine = pyttsx3.init()
model = Model(r"C:\Users\chibo\Downloads\vosk\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

#Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Function to process user commands
def process_command(command):
    if "random" in command:
        response = requests.get("https://www.boredapi.com/api/activity")
        data = json.loads(response.text)
        activity = data["activity"]
        speak(f"The random activity is: {activity}")
    elif "type" in command:
        response = requests.get("https://www.boredapi.com/api/activity")
        data = json.loads(response.text)
        activity_type = data["type"]
        speak(f"The type of activity is: {activity_type}")
    elif "participants" in command:
        response = requests.get("https://www.boredapi.com/api/activity")
        data = json.loads(response.text)
        participants = data["participants"]
        speak(f"The number of participants involved is: {participants}")
    elif "price" in command:
        response = requests.get("https://www.boredapi.com/api/activity")
        data = json.loads(response.text)
        price = data["price"]
        speak(f"The activity costs: {price}")
    elif "key" in command:
        response = requests.get("https://www.boredapi.com/api/activity")
        data = json.loads(response.text)
        key = data["key"]
        speak(f"The unique key of the activity is: {key}")
    elif "accessibility" in command:
        response = requests.get("https://www.boredapi.com/api/activity")
        data = json.loads(response.text)
        accessibility = data["accessibility"]
        speak(f"The accessibility of the activity is: {accessibility}")
    else:
        speak("Sorry, I didn't recognize that command.")

#the loop for continuous listening
while True:
    try:
        mic = pyaudio.PyAudio()
        stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        stream.start_stream()

        while True:
            data = stream.read(2000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                command = result["text"]
                print("User's Command:", command)
                process_command(command.lower())

        stream.stop_stream()
        stream.close()
        mic.terminate()
    except KeyboardInterrupt:
        break
