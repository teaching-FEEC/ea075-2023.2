import speech_recognition as sr
# IMPORTANTE: é necessário baixar a biblioteca SpeechRecognition do python!
# sudo pip3 install SpeechRecognition
# IMPORTANTE: é necessário baixar a biblioteca pyaudio caso vá utilizar o microfone!
# sudo pip3 install pyaudio

reconhecimento = sr.Recognizer()

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