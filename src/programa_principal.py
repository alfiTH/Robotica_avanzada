import Driver
import RPi.GPIO as GPIO
from MPU6050 import *
import time
import signal
import sys



print("---")
print("SCRIPT START")
print("---")

FINCARRERA_D = 27
FINCARRERA_I = 17


def signal_handler(sig,frame):
        GPIO.cleanup()
        sys.exit(0)

def final_izq(channel):
        print("derecha")
        driver.setspeed(0)
        driver.setStateMotor(False)


def final_der(channel):
        print("izquierda")
        driver.setspeed(0)
        driver.setStateMotor(False)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(FINCARRERA_I,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(FINCARRERA_D,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#GPIO.add_event_detect(FINCARRERA_I,GPIO.FALLING,callback=final_izq,bouncetime=100)
#GPIO.add_event_detect(FINCARRERA_D,GPIO.FALLING,callback=final_der,bouncetime=100)

signal.signal(signal.SIGINT,signal_handler)


#----------------------------------------------------------------------
# init MPU6050
#----------------------------------------------------------------------

MPU_Init()
driver = Driver.Driver()
driver.setStateMotor(True)
obj = time.gmtime(0) 
epoch = time.asctime(obj)
P = 1.5
I = 0
D = 0
integral = 0
while True:
    try:

        #Read Accelerometer raw value
        if(abs(Ax := read_raw_data(ACCEL_YOUT_H)/122.5) < 1 ):
              Ax = 0
    except Exception as e:
        print(e)

    #t1 = time.time_ns()


    #print("Time ", time.time_ns() - t1)
    print("inclinacion", Ax) 
    #driver.setspeed(-Ax*P)
    time.sleep(0.05)



print("---")
print("SCRIPT FINISHED")
print("---")
