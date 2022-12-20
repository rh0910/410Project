# blink.py

import machine
import time

led = machine.Pin("LED", machine.Pin.OUT) # "LED" is the on board LED

# blink ten times
for i in range(10):
    print('Blinking... %s' %str(i+1))
    led.toggle()
    time.sleep(0.5)
