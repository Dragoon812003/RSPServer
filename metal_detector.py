import time
import RPi.GPIO as GPIO

def countfreq():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN)
    samples = 1000
    timetotal = 0

    for i in range(samples):
        GPIO.wait_for_edge(17, GPIO.FALLING)
        start = time.time()
        GPIO.wait_for_edge(17, GPIO.FALLING)
        stop = time.time()
        duration = stop - start
        timetotal = timetotal + duration

    timeavg = timetotal / samples
    freq = 1 / timeavg
    return(freq)


# for i in range(100):
#     print(i, ":", countfreq())