import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

def setup():
    IR1 = 3     #right front
    IR2 = 5    #right back
    IL1 = 7    #left front
    IL2 = 11    #left back

    AM1 = 5
    AM2 = 6

    # enable12 = 9
    # enable34 = 10

    gpio.setup(IR1, gpio.OUT)
    gpio.setup(IR2, gpio.OUT)
    gpio.setup(IL1, gpio.OUT)
    gpio.setup(IL2, gpio.OUT)
    # gpio.setup(AM1, gpio.OUT)
    # gpio.setup(AM2, gpio.OUT)
    # pwm = gpio.PWM(40, 100) 
    
    # gpio.output(enable12, pwm)
    # gpio.output(enable34, pwm)

    return IR1, IR2, IL1, IL2, AM1, AM2

def go_forward(IR1, IR2, IL1, IL2):
    gpio.output(IR1, True)
    gpio.output(IR2, False)
    gpio.output(IL1, True)
    gpio.output(IL2, False)

def go_backward(IR1, IR2, IL1, IL2):
    gpio.output(IR1, False)
    gpio.output(IR2, True)
    gpio.output(IL1, False)
    gpio.output(IL2, True)

def go_right(IR1, IR2, IL1, IL2):
    gpio.output(IR1, False)
    gpio.output(IR2, True)
    gpio.output(IL1, True)
    gpio.output(IL2, False)

def go_left(IR1, IR2, IL1, IL2):
    gpio.output(IR1, True)
    gpio.output(IR2, False)
    gpio.output(IL1, False)
    gpio.output(IL2, True)

def stop(IR1, IR2, IL1, IL2):
    gpio.output(IR1, False)
    gpio.output(IR2, False)
    gpio.output(IL1, False)
    gpio.output(IL2, False)

def arm_right_start(AM1, AM2):
    gpio.output(AM1, True)
    gpio.output(AM2, False)

def arm_left_start(AM1, AM2):
    gpio.output(AM1, False)
    gpio.output(AM2, True)

def arm_stop(AM1, AM2):
    gpio.output(AM1, False)
    gpio.output(AM2, False)
    

    