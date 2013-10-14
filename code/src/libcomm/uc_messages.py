""" defines incoming messages from the microcontroller """

incoming_messages = {
0x41: {
    "noms": [
        "switch",
        "chan0",
        "pince_current", # 1
        "bras_bas_current", # 2
        "bras_haut_current", # 3
        "rotation_current", # 4
        "canon_current", # 5
        "wheel_speed_current", # 6 et 7
        "encodeur",
        "adc0",
        "adc1",
        "adc2",
        "adc3"
        ], 
    "facteur": [1,1,1,1,1,1,1,1,1,1,1,1,1], 
    "format": "<BHHHHHHHiHHHH"
    }
}
