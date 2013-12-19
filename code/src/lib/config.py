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
        "a_pin": "P9_33", #RGB1
        "b_pin": "P9_35",
        "c_pin": "P9_36",
        "black_val": [0.020,0.180,0.027],
        "white_val": [0.078,0.230,0.12],
        "orange_val": [0.077,0.22,0.085],
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

