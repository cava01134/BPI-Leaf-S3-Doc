import network, utime

wifi = network.WLAN(network.STA_IF)
wifi.active(False)
wifi.active(True)

while True:
    wifi.connect('SSID','Password') # change Wi-Fi information according to user
    print('Establishing Wi-Fi Connection')
    for i in range(10):
        print('Connecting to Wi-Fi in {}s'.format(i))
        utime.sleep(1)
        if wifi.isconnected():
            break          
    if wifi.isconnected():
        print('WiFi connection OK!')
        print('Network Config =', wifi.ifconfig())
        break
    else:
        print('WiFi Internal Error')
        break
