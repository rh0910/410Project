import machine
import time

# A lot of this was inspired by Arduino code 
# This code was alot transfered to the CrashSendData so that we can use these sensor values to send data.
led = machine.Pin("LED", machine.Pin.OUT) # LED is the onboard LED on the pico
shock = machine.Pin(0, machine.Pin.IN) # 0 is the GP0 pin on the pico. It is an input pin.
buzzer = machine.Pin(1, machine.Pin.OUT) # 1 is the GP1 pin on the pico. It is an output pin becuase the buzzer makes sound.
ir = machine.Pin(2, machine.Pin.IN) # 2 is the GP2 pin on the pico. It is an input pin.
knock = machine.Pin(16, machine.Pin.IN) # 16 is the GP16 pin on the pico. It is an input pin.


def main():
    # Most of the code for connecting to wifi was given by atSign. 
    # Most of the code is explained by atSign. 
    # Look at their readMe for more info. https://github.com/atsign-foundation/at_pico_w/tree/umass2022
    # read settings.json
    from lib.at_client.io_util import read_settings
    ssid, password, atSign = read_settings() # reads the settings given by the settings.json file
    del read_settings

# connect to wifi
    print('Connecting to WiFi %s...' % ssid)
    from lib.wifi import init_wlan
    init_wlan(ssid, password)
    del ssid, password, init_wlan

    # authenticate into server
    from lib.at_client.at_client import AtClient
    atClient = AtClient(atSign, writeKeys=True)
    del AtClient
    atClient.pkam_authenticate(verbose=True)

    key = 'crash' # creates the key crash associated with sensor data
    while (True):
        # gets the boolean value of each sensor. It is either a 0 or 1.
        sval = shock.value() # crash sensor
        irval = ir.value() # ir sensor
        kval = knock.value() # knock sensor
        
        # all the time.sleeps were copy pasted from the test code crash.py. 
        # They are commented out because when we send data it slow so there is no need for delay
        
        # if knock detected
        if kval == 0:
            led.high() # turns on the led on the pico
            print("knock detected")
            #time.sleep(2)
        else: # if not then turn off led on the pico
            led.low() # turns off the led
            # There is not put_public here because the knock sensor detects too fast to actually output anything
            #print("waiting for knock")
            #time.sleep(2)
            
        # if ir detects obstacle
        if irval == 0:
            led.high()
            #print("obstacle detected")
            atClient.put_public(key, "Obstacles Detected.") # sends the data with the key crash
            buzzer.high() # turns on the buzzer
            #time.sleep(0.1)
            buzzer.low() # turns it off
            #time.sleep(0.1)
            
        elif irval == 1 and sval == 1: # if both the ir sensor and crash sensor do not detect anything
            # this is need so it does not say crash detected and no obstacle detected at the same time.
            led.low()
            #print("No obstacles detected")
            atClient.put_public(key, "No Obstacles Detected.") # Sends data

        if sval == 0:
            #print("crash detected")
            led.high()
            buzzer.high()
            #time.sleep(0.5)
            atClient.put_public(key, "Crash detected.") # Sends data
            #break
        else:
            led.low()
            buzzer.low()
        
    #time.sleep(0.5)       

if __name__ == '__main__':
    main()
