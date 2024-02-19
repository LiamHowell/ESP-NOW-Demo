import network
import espnow
from secrets import *
from struct import *

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()   # Because ESP8266 auto-connects to last Access Point

e = espnow.ESPNow()
e.active(True)


def decode_message_host(host_mac, message):
    for peer, value in peers.items():
        if host_mac == value[0]:
            print(value[1], message)
            return peer, unpack(value[1], message)
    return None
   

while True:
    host, msg = e.recv()
    if msg:             # msg == None if timeout in recv()
        hostname, data = decode_message_host(host, msg)
        print(hostname, data)
