from machine import Pin
import camera
import time

led = Pin(4, Pin.OUT)

while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
