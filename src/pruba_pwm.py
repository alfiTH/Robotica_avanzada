import RPi.GPIO as GPIO
from time import sleep

EN_I = 5
EN_D = 6
PWM =13
FRECUENCY = 100

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)         

GPIO.setup(EN_D, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(EN_I, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(PWM, GPIO.OUT, initial=GPIO.LOW)

speed = GPIO.PWM(PWM, FRECUENCY)
speed.ChangeDutyCycle(0)
speed.start(0)

def setspeed(speed):
        if speed < 0:
                if speed < -100:
                        speed = 100
                GPIO.output(EN_I, GPIO.LOW)
                GPIO.output(EN_D, GPIO.HIGH)
                speed.ChangeDutyCycle(abs(speed))          
        elif speed > 0:
                if speed > 100:
                        speed = 100
                GPIO.output(EN_D, GPIO.LOW)
                GPIO.output(EN_I, GPIO.HIGH)
                speed.ChangeDutyCycle(speed)
        print(speed)

while True:    

        for i in range(-25,25,1):
                setspeed(i)
                sleep(1) 
        for i in range(25,-25,-1):
                setspeed(i)
                sleep(1) 

