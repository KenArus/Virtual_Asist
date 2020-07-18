import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import calendar
import random
import wikipedia

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something!')
        audio = r.listen(source)

    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said : '+ data)
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand')
    except sr.RequestError as e:
        print('Request error from Google Speech Recognition'+ e)

    return data

def asisrespond(text):
    print(text)

    myobj = gTTS(text= text, lang='en', slow=False)
    myobj.save('asisrespond_save.mp3')
    os.system('start asisrespond_save.mp3')

def wake_Word(text):
    WAKE_WORDS = ['hi david', 'okay david', 'hello david']
    text = text.lower()

    for pharse in WAKE_WORDS:
        if pharse in text:
            return True
    
    return False

def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day
    month_names = ['January', 'February', 'March', 'April', 'May',
       'June', 'July', 'August', 'September', 'October', 'November',   
       'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', 
                      '7th', '8th', '9th', '10th', '11th', '12th',                      
                      '13th', '14th', '15th', '16th', '17th', 
                      '18th', '19th', '20th', '21st', '22nd', 
                      '23rd', '24th', '25th', '26th', '27th', 
                      '28th', '29th', '30th', '31st']

    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'

def greeting(text):

    GREETING_INPUTS = ['hi', 'hey', 'hola', 'greetings', 'wassup', 'hello']
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'

    return ''

def getPerson(text):
    wordList = text.split()    
    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]

while True:

    text = recordAudio()
    respond = ''

    if (wake_Word(text) == True):
        respond = respond + greeting(text)

        if ('date' in text):
            get_date = getDate()
            respond = respond + '' +get_date
        
        if ('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            respond = respond + ''+ wiki

        asisrespond(respond)

