from TMC_2209_StepperDriver import *
from MPU6050 import *
import time


print("---")
print("SCRIPT START")
print("---")





#-----------------------------------------------------------------------
# initiate the TMC_2209 class
# use your pin for pin_en here
#-----------------------------------------------------------------------
tmc = TMC_2209(21)
#----------------------------------------------------------------------
# init MPU6050
#----------------------------------------------------------------------

MPU_Init()

#-----------------------------------------------------------------------
# set the loglevel of the libary (currently only printed)
# set whether the movement should be relative or absolute
# both optional
#-----------------------------------------------------------------------
tmc.set_loglevel(Loglevel.DEBUG)
tmc.set_movement_abs_rel(MovementAbsRel.ABSOLUTE)
#----------------------------------------------------------------------
# these functions change settings in the TMC register
#-----------------------------------------------------------------------
tmc.set_direction_reg(False)
tmc.set_current(700)
tmc.set_interpolation(True)
tmc.set_spreadcycle(False)
tmc.set_microstepping_resolution(256)
tmc.set_internal_rsense(False)


print("---\n---")

#-----------------------------------------------------------------------
# activate the motor current output
#-----------------------------------------------------------------------
tmc.set_motor_enabled(True)
while True:
	
	#Read Accelerometer raw value
    acc_x = read_raw_data(ACCEL_YOUT_H)
    Ax = acc_x/16384.0
    
    tmc.set_vactual(round(-300000*Ax)) 
    print("Ax = %.2f g" %Ax)
    time.sleep(0.1)



#-----------------------------------------------------------------------
# deactivate the motor current output
#-----------------------------------------------------------------------
tmc.set_motor_enabled(False)

print("---\n---")





#-----------------------------------------------------------------------
# deinitiate the TMC_2209 class
#-----------------------------------------------------------------------
tmc.deinit()
del tmc

print("---")
print("SCRIPT FINISHED")
print("---")
