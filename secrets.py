'''
Dict to store all of the ESP-NOW Values
In the form: Hub Name: [MAC Address, Struct packing string, [Titles for data points]]
'''
peers = {
    "Hub": [b'\x7c\xdf\xa1\xf9\x0d\x24','<ih',['Soil Moisture', 'Battery Voltage']],
    "Soil1": [b'\xdc\xda\x0c\x57\xb4\x0c','<ih']
    }
