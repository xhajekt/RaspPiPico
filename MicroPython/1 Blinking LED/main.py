# Example using PWM to fade an LED.

import time
from machine import Pin, PWM


# Construct PWM object, with LED on Pin(25).
pwm = PWM(Pin(25))

# Set the PWM frequency.
pwm.freq(1000)

# Fade the LED in and out a few times.
duty = 0
direction = 1
num = 0
#for _ in range(256 * 256):
while True:
	duty += direction
	if duty > 255:
		duty = 255
		direction = -1
	elif duty < 0:
		duty = 0
		direction = 1
    #print(duty * duty)
	pwm.duty_u16(num)
	num = duty * duty
	print(num)
	time.sleep(0.001)