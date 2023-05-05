import RPi.GPIO as GPIO
import time 
import signal
import sys

def signal_handler(sig,frame):
	GPIO.cleanup()
	sys.exit(0)
def final_izq(channel):
	print("derecha")
def final_der(channel):
	print("izquierda")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(11,GPIO.FALLING,callback=final_izq,bouncetime=100)
GPIO.add_event_detect(13,GPIO.FALLING,callback=final_der,bouncetime=100)

signal.signal(signal.SIGINT,signal_handler)
signal.pause()
