import machine
import time


led = machine.Pin("LED", machine.Pin.OUT)
shock = machine.Pin(0, machine.Pin.IN)
buzzer = machine.Pin(1, machine.Pin.OUT)
ir = machine.Pin(2, machine.Pin.IN)
knock = machine.Pin(16, machine.Pin.IN)

while True:
    sval = shock.value()
    irval = ir.value()
    kval = knock.value()

    if kval == 0:
        led.high()
        print("knock detected")
        #time.sleep(2)
    else:
        led.low()
        #print("waiting for knock")
        #time.sleep(2)

    if irval == 0:
        led.high()
        print("obstacle detected")
        buzzer.high()
        time.sleep(0.1)
        buzzer.low()
        time.sleep(0.1)
        
    else:
        led.low()
        print("No obstacles detected")
        #time.sleep(2)

    if sval == 0:
        print("crash detected")
        led.high()
        buzzer.high()
        time.sleep(0.5)
        break
    else:
        led.low()
        buzzer.low()
    
    time.sleep(0.5)

buzzer.low()
led.low()
print("crash has occurred")