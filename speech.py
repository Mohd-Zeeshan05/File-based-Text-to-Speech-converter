!sudo apt-get update
!sudo apt-get install -y espeak-ng

import pyttsx3

# Initialize engine
engine = pyttsx3.init()

# Read from file
file_path = "input.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Convert text to speech (plays it)
engine.save_to_file(text, 'output.wav')
engine.runAndWait()

print("Saved speech to output.wav")
