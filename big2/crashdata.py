import machine
import time

led = machine.Pin("LED", machine.Pin.OUT)
shock = machine.Pin(0, machine.Pin.IN)
buzzer = machine.Pin(1, machine.Pin.OUT)
ir = machine.Pin(2, machine.Pin.IN)
knock = machine.Pin(16, machine.Pin.IN)


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
            print("obstacle detected")
            atClient.put_public(key, "Obstacles detected")
            buzzer.high()
            #time.sleep(0.1)
            buzzer.low()
            #time.sleep(0.1)
            
        else:
            led.low()
            #print("No obstacles detected")
            atClient.put_public(key, "No obstacles detected")

        if sval == 0:
            #print("crash detected")
            led.high()
            buzzer.high()
            #time.sleep(0.5)
            atClient.put_public(key, "crash detected")
            #break
        else:
            led.low()
            buzzer.low()
        
    #time.sleep(0.5)       

if __name__ == '__main__':
    main()
