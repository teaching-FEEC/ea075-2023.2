import speech_recognition as sr
import pyttsx3

reconhecimento = sr.Recognizer()

def SoundToText(sound):
    tradutor = pyttsx3.init()
    tradutor.say()
    tradutor.runAndWait

def MicrofoneToText():
    # ao invés de usar o microfone, podemos usar:
    # reconhecimento.energy_threshold = 300
    # audio = sr.AudioFile('audio.wav')
    # with audio as source:
    #   audio = reconhecimento.record(source)
    #   reconhecimento.recognize_google(audio, language='pt-BR')
    with sr.Microphone() as source:
        reconhecimento.adjust_for_ambient_noise(source, duration=0.3)
        print("Pode falar que eu enbtendo... acho!")
        print("Por favor, ao falar uma vogal, diga a palavra 'letra' antes")
        audio = reconhecimento.listen(source)
        try:
            texto = reconhecimento.recognize_google(audio, language='pt-BR')
            print("Você disse: ", texto)
        except sr.UnknownValueError:
            print("Vish, tendi foi nada!")

MicrofoneToText()