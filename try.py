
import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning")
        print("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
        print(",Good Afternoon")
    else:
        speak(",Good Evening")
        print("Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-ng')
            print(f"user said:{statement}\n")

        except Exception as except:
            return "None"
        return statement


wishMe()
speak("i am")

# print(thought = [statement])


if __name__ == '__main__':

    while True:
        #speak("Welcome Dr. Bisallah Hashim the H O D of computer science")
        #speak("Welcome Prof. Abdul-Rasheed Na'Allah the vice chancellor of University of Abuja")
       # speak("Tell me how can I help you?") or
        speak("How may i be of assistant to you")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your  assistant MASTER JOHN is shutting down,Good bye')
            print('your personal assistant MASTER JOHN is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'google' in statement:
            speak('Searching Google...')
            statement = statement.replace("google", "")
            results = google.summary(statement, sentences=3)
            speak("According to Google")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am MASTER JOHN version 1 point O your persoanl assistant. I am programmed to perform minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'in different cities , get top headline news from times of USA and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Nodestech")
            print("I was built by Nodestech")

        elif "who is the vice chancellor of University of Abuja" in statement:
            speak("The vice Chancellor of the University of Abuja is Prof. Abdul-Rasheed Na'Allah, he hails from Kwara state in Nigeria")
            print("The vice Chancellor of the University of Abuja is Prof. Abdul-Rasheed Na'Allah, he hails from Kwara state in Nigeria")

        elif "who is the Head of Department of Computer Science" in statement:

            speak(
                "The current Head of Department of Computer Science is Doctor Hashim Bisallah")
            print(
                "The current Head of Department of Computer Science is Doctor Hashim Bisallah")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab(
                "https://www.latestnigeriannews.com/today/vanguard/nigeria-vanguard-newspaper-headlines-today")
            speak('Here are some headlines news from Nigeria,Happy reading')
            time.sleep(6)

       # elif "camera" in statement or "take a photo" in statement:
           # ec.capture(0,"robo camera","img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak(
                "Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
