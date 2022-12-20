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
    atClient = AtClient(atSign)
    del AtClient
    atClient.pkam_authenticate(verbose=True)

    for i in range(50000):
        key = 'instructions'
        appAtsign = '@initialcomputer'
        data = atClient.get_public(key, appAtsign)
        print(data)
        

if __name__ == '__main__':
    main()