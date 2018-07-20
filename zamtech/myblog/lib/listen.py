import speech_recognition as sr
import pyttsx3

#pyttsx3 engine
engine = pyttsx3.init('espeak')
engine.getProperty('rate')
engine.setProperty('rate', 100)

class listening():
    spoken = ""
    spoken2 = ""
    while spoken != "stop listening now":
        # Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source, phrase_time_limit=0)

        # Speech recognition using Google Speech Recognition

        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            spoken = r.recognize_google(audio)
            spoken2 = spoken2 + " " + spoken
            print(spoken)
            engine.say(spoken)
            engine.runAndWait()
        except sr.UnknownValueError:
            print("...")
        except sr.RequestError as e:
            print("Could not request results from Speech Recognition service; {0}".format(e))
    print(spoken2)