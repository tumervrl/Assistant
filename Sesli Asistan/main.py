import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import os
import random



r = sr.Recognizer()

def kayit(ask=False):
    with sr.Microphone() as source:
        if ask:
            konusma(ask)

        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            konusma('Anlaşılmadı, Tekrarlar mısın?')
        except sr.RequestError:
            konusma("Sistem Çalışmıyor")
        return voice


def cevap(voice):
    if 'nasılsın' in voice:
         konusma("İyiyim Sen Nasılsın ?")
    if 'saat kaç' in voice:
        konusma(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = kayit('Aramak istediğin şey nedir?')
        url = 'https://google.com.tr/search?q='+search
        webbrowser.get().open(url)
        konusma(search + 'için bulduğum şeyler')
    if 'programı bitir' in voice:
        konusma('Tamamdır, Görüşürüz.')
        exit()


def konusma(string):
    TTS = gTTS(string, lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    TTS.save(file)
    playsound(file)
    os.remove(file)



konusma('Merhaba, Nasıl Yardımcı Olabilirim ?')
time.sleep(1)
while 1:
    voice = kayit()
    print(voice)
    cevap(voice)