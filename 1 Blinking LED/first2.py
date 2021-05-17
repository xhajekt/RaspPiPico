import machine
import time

led_ext = machine.Pin(15, machine.Pin.OUT)
led_int = machine.Pin(25, machine.Pin.OUT)

while True:
    led_ext.toggle()
    led_int.toggle()
    time.sleep(0.5)
    