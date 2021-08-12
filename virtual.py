import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
# from ecapture import ecapture as ec
import wolframalpha
import json
import requests


print('I am MASTER JOHN, University of Abuja, Virtual assistant ')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-gb')
            print(f"user said:{statement}\n")

        except Exception as e:
            return "None"
        return statement


speak("I am MASTER JOHN, University of Abuja Virtual assistant")

wishMe()

speak("Let me tell you about the University of Abuja")

speak("The University of Abuja, was established, in January 1988, out of the need to provide, an institution of, higher learning, within Abuja, the new Federal Capital,"

      "whose objectives will be in stride,"

      "with the ideals that informed, the conception of the city.,"

      "The  matriculation, of pioneer students of, the University in 1990 marked, the beginning of its academic,"

      "work in its mini campus, Gwagwalada., In the same year, the University was allocated, an expanse of land,"

      "covering over 11,824 hectares, along Abuja-Airport, Road for the, development of its main campus., While development, of structures continued to grow,"

      "on the main campus of the University,  it has continued, to run  its regular, programmes in the mini campus, and its distance learning, programmes in Area 3 Garki.,"

      "To the Glory of God, most of the, University’s Faculties and the, Centre for Distance Learning,  have  now relocated to the, permanent site of the University,"

      "which is located less than,  ten minutes drive,  from the Nnamdi Azikwe, International Airport. ")

speak("the current vice chancellor of the university is, Prof. Abdul-Rasheed Na'Allah ")

speak("The University provides educational opportunities to all persons without distinction of race, gender, or political convictions,"

      "thus it is regarded as the University for National Unity, located in the centre of unity.'"

      "The University of Abuja has abundant potential, because of its favoured location, in the heart of the country.")

speak("Our Vision: To develop, an institution of, higher learning that, combines academic excellence with, the pursuit of the unity of Nigeria.")

speak("Our Mission: (1). To encourage the advancement of learning and, to hold out to all person, without distinction of race, creed, sex or political conviction, the opportunity of, acquiring higher liberal education;"

      "(2). To provide courses of instruction, and other facilities for the pursuit, of learning in all its branches. "

      "(3). To encourage and, promote scholarship, and conduct research in all fields, of learning and human endeavor. To relate its, activities to the social, cultural and economic, needs of the people of Nigeria."

      "(4). To undertake as part, of its academic, programmes distance, learning and continuing, education in various disciplines "

      "(5). To cater for the, interest of working, class or those who cannot, benefit from the full-time, university education, and to undertake, any other activities, appropriate for a University, of the highest standard.")


if __name__ == '__main__':

    while True:
        # speak("Welcome Dr. Bisallah Hashim the H O D of computer science")
        # speak("Welcome Prof. Abdul-Rasheed Na'Allah the vice chancellor of University of Abuja")
       # speak("Tell me how can I help you?") or

        speak("How may i be of help?")
        print("How may i be of help?")

        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your  assistant, MASTER JOHN, is shutting down,Good bye')
            print('your assistant, MASTER JOHN, is shutting down,Good bye')
            break

        if 'what is' in statement or 'where is' in statement:
            speak('please wait...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak(" ")
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
            speak('I am, MASTER JOHN, version, 1 point O university of abuja, vitual assistant. I am programmed to, perform minor tasks like,'

                  'opening youtube, tell you about the university of abuja, and also the, department of, of computer, science, google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'

                  'in different cities , get top headline news, from top Nigeria, news agencies, and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built, by Computer Science, Research Team")
            print("I was built by Computer Science Research Team")

        elif "who is the vc of university of abuja" in statement:

            speak("The vice Chancellor of the University of Abuja, is Prof. Abdul-Rasheed Na'Allah, he hails from Kwara state in Nigeria")
            print("The vice Chancellor of the University of Abuja, is Prof. Abdul-Rasheed Na'Allah, he hails from Kwara state in Nigeria")

        elif "who is the head of department of computer science" in statement:

            speak(
                "The current Head of Department of Computer Science is Doctor Hashim Bisallah")
            print(
                "The current Head of Department of Computer Science is Doctor Hashim Bisallah")

        elif "what are the achievement of the vice chancellor in his two years of stay in office" in statement or "what has the v c achieve so far in the school" in statement or "what has the v c done so far in the school" in statement:
            speak("")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab(
                "https://www.latestnigeriannews.com/today/vanguard/nigeria-vanguard-newspaper-headlines-today")
            speak('Here are some headlines news, from Nigeria, Happy reading')
            time.sleep(6)

       # elif "camera" in statement or "take a photo" in statement:
           # ec.capture(0,"robo camera","img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'tell me about computer science' in statement:
            speak(
                "Let me give you, The breif History of the Department of Computer Science.")

            speak("The Department was established, in February, 1991, and the current head of department, is Dr. Hashim Bisallah. it currently has, 20 full time, and 5 adjunct  academic staff. the current population of students, is 690 spread across 100 level to the 5th session.")

            speak("Our Mission:, is to develop, and impact knowledge, and skills, in the feild of computer science")

            speak("Our vision:, 1. An influential role in industry, and the information technology community, 2. Sustaining high respect, for its research, and undergraduate education, 3. Empowering our graduates, with the vision and confidence, required to become innovative, ICT leaders and techprenuers. ")

            speak("we offer admission into  BSC, PGD, MSC and PHD, in computer science.")

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
