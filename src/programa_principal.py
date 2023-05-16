import Driver

import BNO055
import RPi.GPIO as GPIO
import time
import signal
import sys



print("---")
print("SCRIPT START")
print("---")

FINCARRERA_D = 17
FINCARRERA_I = 27


def signal_handler(sig,frame):
        GPIO.cleanup()
        sys.exit(0)

def final_izq(channel):
        print("izquierda")
        driver.setSpeed(0)
        driver.setStateMotor(False)
        sys.exit(0)



def final_der(channel):
        print("derecha")
        driver.setSpeed(0)
        driver.setStateMotor(False)
        sys.exit(0)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(FINCARRERA_I,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(FINCARRERA_D,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#GPIO.add_event_detect(FINCARRERA_I,GPIO.FALLING,callback=final_izq,bouncetime=100)
GPIO.add_event_detect(FINCARRERA_D,GPIO.FALLING,callback=final_der,bouncetime=100)

signal.signal(signal.SIGINT,signal_handler)


#----------------------------------------------------------------------
# init MPU6050
#----------------------------------------------------------------------

bno = BNO055.BNO055()
if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')
status, self_test, error = bno.get_system_status()
print('System status: {0}'.format(status))
print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
if status == 0x01:
    print('System error: {0}'.format(error))
    print('See datasheet section 4.3.59 for the meaning.')

# Print BNO055 software revision and other diagnostic data.
sw, bl, accel, mag, gyro = bno.get_revision()
print('Software version:   {0}'.format(sw))
print('Bootloader version: {0}'.format(bl))
print('Accelerometer ID:   0x{0:02X}'.format(accel))
print('Magnetometer ID:    0x{0:02X}'.format(mag))
print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))

driver = Driver.Driver()
driver.setStateMotor(True)
obj = time.gmtime(0) 
epoch = time.asctime(obj)
P = 25
I = 0
D = 0
integral = 0
while True:
    try:
        #heading, roll, pitch = bno.read_euler()
        x,y,z,w = bno.read_quaternion()
        speed = (y+0.0025)/0.004
    except Exception as e:
        print(e)

    #t1 = time.time_ns()
    # Print everything out.

    #print("Time ", time.time_ns() - t1)
    print("inclinacion", speed) 
    driver.setSpeed(speed*P)
    time.sleep(0.01)



print("---")
print("SCRIPT FINISHED")
print("---")
