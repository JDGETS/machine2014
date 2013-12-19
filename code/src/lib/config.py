devices = {
    "vacuum": {
        "pin": "P9_15" # Out 1
    },
    "white_piston": {
        "pin": "P9_22", #Servo1
        "pull_duty": 4.6,#TODO CALIBRATE
        "standby_duty": 6.3,
        "push_duty": 7.5
    },
    "orange_piston": {
        "pin": "P9_14", #Servo0
        "pull_duty": 4.5,
        "standby_duty": 6.2,
        "push_duty": 7.7
    },
    "color_sensor": {
        "a_pin": "P9_39", #RGB1
        "b_pin": "P9_40",
        "c_pin": "P9_37",
        "black_val": [0.010644444115459919, 0.014177777767181397, 0.022111111506819724],
        "white_val": [0.065244445204734797, 0.064688889533281321, 0.098844445347785956],
        "orange_val": [0.023955555856227873, 0.073466666638851166, 0.078111109435558324],
        "error": 0.02
    }
    ,
     "vacuum_servo": {
        "pin": "P9_42", #Servo3
        "pull_duty": 4.5, #TODO CALIBRATE
        "standby_duty": 4.5,
        "push_duty": 4.5
    },
    "gate_servo": {
        "pin": "P8_13", #Servo2
        "pull_duty": 9.4, #TODO CALIBRATE
        "standby_duty": 10.5,
        "push_duty": 11.5
    }
}

