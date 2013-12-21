devices = {
    "white_piston": {
        "pin": "P9_22", #Servo1
        "pull_duty": 5.6,
        "standby_duty": 6.3,
        "push_duty": 7.5
    },
    "orange_piston": {
        "pin": "P9_14", #Servo0
        "pull_duty": 5.6,
        "standby_duty": 6.3,
        "push_duty": 7.5
    },
    "vacuum_servo": {
        "pin": "P9_42", #Servo3
        "pull_duty": 8,
        "standby_duty": 5,
        "push_duty": 2.8
    },
    "gate_servo": {
        "pin": "P8_13", #Servo2
        "pull_duty": 9.4, #TODO CALIBRATE
        "standby_duty": 10.5,
        "push_duty": 11.5
    },
    "color_sensor": {
        "a_pin": "P9_39", #RGB1
        "b_pin": "P9_40",
        "c_pin": "P9_37",
        "black_val": [0.010644444115459919, 0.014177777767181397, 0.022111111506819724],
        "white_val": [0.065244445204734797, 0.064688889533281321, 0.098844445347785956],
        "orange_val": [0.023955555856227873, 0.073466666638851166, 0.078111109435558324]
    },
    "spawn_switch": {
        "pin": "P8_12" # In2
    },
    "start_collect_switch": {
        "pin": "P8_16" # In4
    },
    "load_tank_switch": {
        "pin": "P8_14" # In3
    },
    "stepper_rail":{
        "pin":"GPIO2_6",
        "direction":"P8_43",
        "reset":"P8_44",
        "enable":"P8_46"
     },
     "rail":{
         "switch_away": "",
         "switch_home": ""#Switch
         "switch_stand":""
     },
    "camion":{
        "foot_standby_time":"3",
        "stepper_start_position_ticks": (5.0/5000) * 1.0,
        "stepper_foot_complete_ticks": (5.0/5000) * 20.5, #20.5' <- Distance foot to floor
     },
    "camion_collector_switch":{
        "pin":"P8_12",
     },
    "camion_dump_switch":{
        "pin":"P8_14",
     },
    "camion_foot_up_switch":{
        "pin":"P8_16",
     },
    "camion_stepper":{
        "pin":"GPIO2_6",
        "direction":"P8_43",
        "reset":"P8_44",
        "enable":"P8_46"
    },
}
