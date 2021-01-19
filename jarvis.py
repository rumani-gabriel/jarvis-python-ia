import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
sp_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
engine.setProperty('voice', sp_voice_id)
engine.setProperty('rate', 130)


""" definimos lo que nos va a decir de manera hablada"""
def speak (audio):
    engine.say(audio)
    engine.runAndWait()


""" damos la estructura del tiempo en horas, minutos y segundos"""
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time) 

""" definimos los ítems que van a llevar nuestra consulta de la fecha"""
def date():
    year= int (datetime.datetime.now().year)
    mont= int (datetime.datetime.now().month) 
    date= int (datetime.datetime.now().day)  
    speak(date)
    speak(mont)
    speak(year)
"""es el saludo inicial, dependiendo la hora, varía el saludo"""
def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        #speak("good mornig sir!")
        speak("Buenos días, Gabi")
    elif hour >= 12 and hour <18:
        #speak ("good afternon sir")
        speak ("Buenas tardes, Señor!")
    elif hour >=18 and hour < 24:
        speak ("hola, amo del universo")
    else:
        speak("buenas noches Gabi")
        
    # speak("please tell me how can i help you?")
    speak(" Aquí Yarvis...¿En qué puedo ayudarlo?")
    
""" con ésta función, podemos acceder a enviar mails"""
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login ('youremail@gmail.com', 'password') #por razones muy claras no pongo mi password
    server.sendmail ("rumani.gabriel@gmail.com", to, content)
    server.close()   

"""reconocimiento de la orden por voz"""
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("listening...")
        print ("Escuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
  
    try:
        # print ("recongnizning...")
        print ("reconociendo..")
        query = r.recognize_google (audio, language ='es-MX')
        print(query)
           
                
                    
            
    except Exception as e:
        print(e)
        # speak("say that again, please...")
        speak("no podré ayudarte")
        query= None 
                       
    return query
        
        
"""aquí se guardan todos los comandos de voz, cada consulta tiene asignada una respuesta"""
def main():
    
    query = takeCommand()
    
    if 'wikipedia' in query.lower():
        # speak('searching in Wikipedia...')
        wikipedia.set_lang("es")  
        speak('Buscando en Wikipedia...')
        query = query.replace("wikipedia", "")        
        results = wikipedia.summary (query, sentences = 2)
        print (results)
        speak(results)
        speak("Algo más, señor?")
        main()
        
        #'open youtube'
    elif 'abre youtube' in query.lower():
        url="youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak("Hecho, algo más?")
        main()
        
        #'open google'
    elif 'abre google' in query.lower():
        url="google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak("lo he realizado... ¿Puedo hacer algo más?...")
        main()
    
    elif 'abre mercado libre' in query.lower():
        url="mercadolibre.com.ar"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak("lo he realizado... ¿Puedo hacer algo más?...")
        main()        
        
    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\Gabriel\\Downloads\\discos descargados" 
        songs = os.listdir(songs_dir)
        print (songs)
        os.startfile(os.path.join(songs_dir , songs[0]))
        #'the time'
    elif 'la hora' in query.lower():
        strTime = datetime.datetime.now().strftime("%I:%M:%S")
        speak(f"la hora es {strTime}")
        speak("¿desea algo más?")
        main()

    elif 'email a Gabi' in query.lower():
        try:
            speak("what should I send?")
            content = takeCommand()
            to = "rumani.gabriel@gmail.com"
            sendEmail(to, content)
            speak ("Email has been sent successfully")
            
        except Exception as e:
            print (e)
    elif 'cómo estás' in query.lower():
        speak ("muy bien, muy contenta que me hayas programado... ¿En qué puedo ayudarte?")
        main()
    elif 'nada más' in query.lower():
        speak("fué un placer servirte... Hasta luego.")   
    elif 'opinas de mí' in query.lower():
        speak("Creo que es una persona muy determinada, que no conoce el término rendirse. Cualquier empresa haría muy bien en darle una oportunidad.") 

wishme()
main()
    