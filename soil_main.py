import network
import espnow
from time import sleep
from secrets import *
from struct import *

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()      # For ESP8266

e = espnow.ESPNow()
e.active(True)
hub = peers['Hub'][0]   # MAC address of peer's wifi interface
e.add_peer(hub)      # Must add_peer() before send()


################ SOME TESTING
# Data to send from a soil node
# [soil moisture (Raw ADC), battery voltage, misc sensor data]
ex_soil = 65536
ex_batt_volt = 3.4 # MULTIPLY BY 10/100
calc_ex_batt_volt = int(ex_batt_volt*100)

pack_str = '<ih'

inpt = pack(pack_str, ex_soil, calc_ex_batt_volt)
print(inpt)

e.send(hub, inpt)

outp = unpack(pack_str, inpt)

print(outp)
