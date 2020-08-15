'''import speech_recognition as sr #pip install SpeechRecognition and pip install pyaudio
r = sr.Recognizer()

with sr.Microphone() as source:
  print('speak Anything: ')
  audio = r.listen(source)
  try:
    text = r.recognize_google(audio)
    print('You said: {}'.format(text))
  except sr.UnknownValueError:
    print('Sorry could not recognize your voice')
  except sr.RequestError:
    print("My Speech service is down")  
        '''
import speech_recognition as sr
from time import ctime 
import webbrowser
from gtts import gTTS
import os
import random
import playsound

# pip install SpeechRecognition 
# sudo apt-get install portaudio19-dev python-pyaudio python3-pyaudio and 
# pip install pyaudio
# pip install gTTS to get the response in audio in place of text and to do this 
# we need to install playsound using pip which will ristrict gTTS to play the audiousing player.
r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        alexis_speak('How can i help you? ')
        audio = r.listen(source) # listen method is going to get the source voice 
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio) # recognize_google method  actually recognize the voice 
            #print('You said: {}'.format(text))
        except sr.UnknownValueError:
            alexis_speak('Sorry could not recognize your voice')
        except sr.RequestError:
            alexis_speak("My Speech service is down")  
        return voice_data  

def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('My name is Alexa')
    if 'what time is it' in voice_data:
        alexis_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Here is what i found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Here is location i found for ' + location)    

voice_data = record_audio()
print(voice_data)  
respond(voice_data)




