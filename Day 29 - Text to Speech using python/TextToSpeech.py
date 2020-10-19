import pyttsx3
engine = pyttsx3.init()

rate = engine.getProperty('rate')
#print(rate)
engine.setProperty('rate', 125)

voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)
#engine.setProperty('voice',voices[1].id)

value = input(" Please enter your text : ")
engine.setProperty('volume',5.0) 

engine.say(value)
#engine.save_to_file(value, 'dhanush_test_audio.mp3')

engine.runAndWait()
engine.stop()