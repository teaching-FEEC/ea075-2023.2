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
        print("Pode falar que eu entendo... acho!")
        print("Por favor, ao falar uma vogal, diga a palavra 'letra' antes")
        audio = reconhecimento.listen(source)
        try:
            texto = reconhecimento.recognize_google(audio, language='pt-BR')
            print("Você disse: ", texto)
        except sr.UnknownValueError:
            print("Vish, tendi foi nada!")

MicrofoneToText()


"""
VERSÃO PARCIAL DO CÓDIGO!
# VERSÃO NO WOKWI (.Ino, sem o speech_recognition, apenas com pull up button e o servo)
# Check: https://wokwi.com/projects/382227933754090497


# Código abaixo: Versão parcial, sem movimentação dos servos!!!
# Ainda preciso testar se passar o PIN do microfone como source dá certo (def MicrofoneToText())

from machine import Pin, ADC, PWM
from utime import sleep
import speech_recognition as sr

# IMPORTANTE: é necessário baixar a biblioteca SpeechRecognition do python!
# sudo pip3 install SpeechRecognition

# IMPORTANTE: é necessário baixar a biblioteca pyaudio caso vá utilizar o microfone!
# sudo pip3 install pyaudio

print("Hello, ESP32!")

angle =0
reconhecimento = sr.Recognizer()
mic = ADC(Pin(34))
button = Pin(25, Pin.IN, Pin.PULL_UP, hold=True)
servo = PWM(Pin(23), freq=500, duty=256)

def MicrofoneToText():
    with mic as source:                                                         # TESTAR!
        reconhecimento.adjust_for_ambient_noise(source, duration=0.3)
        print("Pode falar que eu enbtendo... acho!")
        print("Por favor, ao falar uma vogal, diga a palavra 'letra' antes")
        audio = reconhecimento.listen(source)
        try:
            texto = reconhecimento.recognize_google(audio, language='pt-BR')
            print("Você disse: ", texto)
            return texto
        except sr.UnknownValueError:
            print("Vish, tendi foi nada!")
            return ""

mic.atten(ADC.ATTN_11DB)
while True:
    if button.value() == 1:
        while button.value() == 1:
            fala = MicrofoneToText()
            if fala.lower == "letra a":
                print("a")
            elif fala.lower == "letra e":
                print("e")
            elif fala.lower == "letra i":
                print("i")
            elif fala.lower == "letra o":
                print("o")
            elif fala.lower == "letra u":
                print("u")
        else:
            continue
    else:
        continue
"""