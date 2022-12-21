import machine
import time

# A lot of this was inspired by Arduino code 
led = machine.Pin("LED", machine.Pin.OUT) # LED is the onboard LED on the pico
shock = machine.Pin(0, machine.Pin.IN) # 0 is the GP0 pin on the pico. It is an input pin.
buzzer = machine.Pin(1, machine.Pin.OUT) # 1 is the GP1 pin on the pico. It is an output pin becuase the buzzer makes sound.
ir = machine.Pin(2, machine.Pin.IN) # 2 is the GP2 pin on the pico. It is an input pin.
knock = machine.Pin(16, machine.Pin.IN) # 16 is the GP16 pin on the pico. It is an input pin.

# while true to keep it running
while True:
    # all these get the current value of each sensor
    # those values are boolean so 0 or 1.
    sval = shock.value()
    irval = ir.value()
    kval = knock.value()
    
    if kval == 0:
        led.high() # if the led value is low set it to high then print out if it was detected
        # .high changes the value to 1 
        print("knock detected")
        #time.sleep(2)
    else:
        led.low()
        # below will print out waiting for knock if we do not see one
        #print("waiting for knock")
        #time.sleep(2)

    if irval == 0:
        # again similar to above. Turns on the LED if we detect something on the ir obstacle detector
        led.high()
        print("obstacle detected")
        buzzer.high() # turns on the buzzer
        time.sleep(0.1) # turns on the buzzer for a little bit of time
        buzzer.low() # turns it off
        time.sleep(0.1) # delays again
        # these are used to make the beep of the buzzer not last too long. IT IS VERY LOUD.
        
    else:
        led.low()
        print("No obstacles detected")
        #time.sleep(2)

    if sval == 0:
        print("crash detected") # again if the crash sensor is hit then we print this out.
        # A lot of the code is similar. We just turn on the buzzer if the crash is detected.
        led.high() 
        buzzer.high()
        time.sleep(0.2)
        buzzer.low()
        #break
    else:
        led.low()
        buzzer.low()
    
    time.sleep(0.5)
# this code below here is used when i uncomment the break in sval.
buzzer.low()
led.low()
print("crash has occurred")
