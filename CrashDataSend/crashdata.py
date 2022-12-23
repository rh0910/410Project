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
    # read settings.json
    from lib.at_client.io_util import read_settings
    ssid, password, atSign = read_settings()
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

    key = 'crash'
    while (True):
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
            #print("obstacle detected")
            atClient.put_public(key, "Obstacles Detected.")
            buzzer.high()
            #time.sleep(0.1)
            buzzer.low()
            #time.sleep(0.1)
            
        elif irval == 1 and sval == 1:
            led.low()
            #print("No obstacles detected")
            atClient.put_public(key, "No Obstacles Detected.")

        if sval == 0:
            #print("crash detected")
            led.high()
            buzzer.high()
            #time.sleep(0.5)
            atClient.put_public(key, "Crash detected.")
            #break
        else:
            led.low()
            buzzer.low()
        
    #time.sleep(0.5)       

if __name__ == '__main__':
    main()
