import pyttsx3 as tts

speaker = tts.init()
voices = speaker.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

speaker.say("Hello this is python")
speaker.runAndWait()