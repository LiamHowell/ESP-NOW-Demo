# Code written using ChatGPT

import network
import ubinascii

# Connect to WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# Retrieve and format MAC address
mac_bytes = wifi.config('mac')
mac_address = "b'" + ''.join("\\x{:02x}".format(x) for x in mac_bytes) + "'"


# Print formatted MAC address
print("MAC Address: \n", mac_address)
