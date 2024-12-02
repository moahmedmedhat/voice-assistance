import datetime
import time
import os
from gtts import gTTS
import playsound
import speech_recognition as sr
import weather
x=datetime.datetime.now()
# time=x.strftime("%A %B %d %H:%M:%S %Y")

def speak(text):
    talk=gTTS(text=text,lang='ar')
    filename='file.mp3'
    talk.save(filename)
    playsound.playsound(filename)
    
def get_audio():
    s=sr.Recognizer()
    # print("recognize_google" in dir(s))
    with sr.Microphone() as mic:
        audio=s.listen(mic)
        said=""
        try:
            said=s.recognize_google(audio,language='ar')
            
            # print(said.encode('utf-8'))
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
        except sr.RequestError as e:
            print(f"Request error from Google Speech Recognition: {e}")
            
    return said
            
    


while True:
    text=get_audio()
    wakeup='حمودي'
    print(text)
    if 'حمودي' in text:
        speak('معاك يا اخطبوط')
        
        while True:
            text=get_audio()
            print(text)
            if any(word in text for word in ['ازيك', 'عامل', 'كيف حالك']):
                speak('الحمد لله كله تمام')
                text=' '

            if any(word in text for word in ['الوقت','الساعه']):   
                time=x.strftime("%H:%M:%S")
                print(time)
                speak(time)
                text=' '
            
            if any(word in text for word in ['التاريخ','تاريخ']):   
                time=x.strftime("%B %d %Y")
                print(time)
                speak(time)
                text=' '
                
            
            if any(word in text for word in ['النهارده ايه','اليوم','يوم']):   
                x=datetime.datetime.now()
                time=x.strftime("%A")
                print(time)
                speak(time)
                text=' '
                
            if 'افتح كود' in text:
                speak('حاضر')
                os.system('code')
            
            if 'حراره' in text or 'الحراره' in text :
                temp=weather.weather()
                print(temp)
                speak(temp)
            
            if 'شكرا' in text:
                speak('حبيبى انت تأمر')
            
            
            if 'اخرج' in text or 'يلا سلام' in text:
                speak(' سلام')
                break
        break
            

    