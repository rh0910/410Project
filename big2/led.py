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

    key = 'led'
    value = 0
    for i in range(5000):

        if value == 0:
            value = 1
        elif value == 1:
            value = 0

        atClient.put_public(key, str(value))


if __name__ == '__main__':
    main()
