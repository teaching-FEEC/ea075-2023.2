"""
VERSÃO PARCIAL DO CÓDIGO!
# VERSÃO NO WOKWI: utilizamos Micropython e apenas 1 servo motor para teste

# Como no wokwi não achamos o componente de microfone para ESP32, replicamos o componente da arduino
# Não há suporte do wokwi na versão livre para importação de bibliotecas (SpeechRecognition, pyaudio)
# As partes referentes ao uso do microfone foram comentadas 

# Check: https://wokwi.com/projects/383069732344217601

# Nos baseamos no uso do SpeechRecognition no RaspberryPy para referenciamento do Pin de microfone (def MicrofoneToText())

CÓDIGO ABAIXO -----------------------------------------------------------------------------------------------
"""

from utime import sleep
from machine import Pin, ADC, PWM
import network
import time

# import speech_recognition as sr
# Speech recognition setup
# recognizer = sr.Recognizer()

# IMPORTANTE: é necessário baixar a biblioteca SpeechRecognition do python!
# sudo pip3 install SpeechRecognition
# IMPORTANTE: é necessário baixar a biblioteca pyaudio caso vá utilizar o microfone!
# sudo pip3 install pyaudio

print("Hello, ESP32!")

print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print(" Connected!")

#reconhecimento = sr.Recognizer()
#mic = ADC(Pin(34), Pin.IN)
#mic.atten(ADC.ATTN_11DB)
button = Pin(13, Pin.IN, Pin.PULL_UP)
servo = PWM(Pin(23), freq=50)
led = Pin(15, Pin.OUT)

'''
def MicrofoneToTextToServo():

    # Cria uma instância de Microphone no pino do MIC (ref.: Raspberry)
    with sr.Microphone(mic) as source:
        
        reconhecimento.adjust_for_ambient_noise(source, duration=0.3)
        print("Pode falar que eu entendo... acho!")
        print("Por favor, ao falar uma vogal, diga a palavra 'letra' antes")
        
        audio = reconhecimento.listen(source)

        try:
            texto = reconhecimento.recognize_google(audio, language='pt-BR')

            if texto.lower == "letra a":
                servo.duty(45)
                time.sleep(0.3)
            elif texto.lower == "letra e":
                servo.duty(60)
                time.sleep(0.3)
            elif texto.lower == "letra i":
                servo.duty(75)
                time.sleep(0.3)
            elif texto.lower == "letra o":
                servo.duty(90)
                time.sleep(0.3)
            elif texto.lower == "letra u":
                servo.duty(105)
                time.sleep(0.3)
        
        except sr.UnknownValueError:
            print("Vish, tendi foi nada!")
'''

def Testando():
    servo.duty(25)
    time.sleep(1)
    servo.duty(45)
    time.sleep(1)
    servo.duty(65)
    time.sleep(1)
    servo.duty(85)
    time.sleep(1)
    servo.duty(105)
    time.sleep(1)
    servo.duty(125)
    time.sleep(1)

while True:
    logic_state = button.value()
    if logic_state == True:
        led.on()
    else:
        led.off()
        Testando()
        #MicrofoneToTextToServo()
