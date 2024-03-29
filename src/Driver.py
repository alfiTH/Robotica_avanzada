import RPi.GPIO as GPIO
import time
EN_I = 6
EN_D = 5
PWM =13
FRECUENCY = 100

class Driver:
    
    
    def __init__(self):
        

        GPIO.setup(EN_D, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(EN_I, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(PWM, GPIO.OUT, initial=GPIO.LOW)

        self.PWMspeed = GPIO.PWM(PWM, FRECUENCY)
        self.PWMspeed.ChangeDutyCycle(0)
        self.PWMspeed.start(0)
        self.motorEnable = False

    def setStateMotor(self, state):
            self.motorEnable = state

    def getStateMotor(self):
        return self.motorEnable

    def touchLimit(self, I_D):
        if I_D :
            GPIO.output(EN_I, GPIO.LOW)
            GPIO.output(EN_D, GPIO.HIGH)
            self.PWMspeed.ChangeDutyCycle(100)          
        else:
            GPIO.output(EN_D, GPIO.LOW)
            GPIO.output(EN_I, GPIO.HIGH)
            self.PWMspeed.ChangeDutyCycle(100)
        time.sleep(5)
        GPIO.output(EN_D, GPIO.LOW)
        GPIO.output(EN_I, GPIO.LOW)
        self.PWMspeed.ChangeDutyCycle(0)

               
    def setSpeed(self, speed):
            if self.motorEnable:
                    if speed < 0:
                            if speed < -100:
                                    speed = 100
                            GPIO.output(EN_I, GPIO.LOW)
                            GPIO.output(EN_D, GPIO.HIGH)
                            self.PWMspeed.ChangeDutyCycle(abs(speed))          
                    elif speed > 0:
                            if speed > 100:
                                    speed = 100
                            GPIO.output(EN_D, GPIO.LOW)
                            GPIO.output(EN_I, GPIO.HIGH)
                            self.PWMspeed.ChangeDutyCycle(speed)
                    else:
                            GPIO.output(EN_D, GPIO.LOW)
                            GPIO.output(EN_I, GPIO.LOW)
                            self.PWMspeed.ChangeDutyCycle(0)
                    print(speed)
