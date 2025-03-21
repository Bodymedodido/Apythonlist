from machine import Pin
import time

led1=Pin(2,Pin.OUT)
while True:
    led1.value(1)
    time.sleep(0.75)
    led1.value(0)
    time.sleep(0.25)

