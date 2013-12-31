devices = {
    # Used by collector/sorter
    "white_piston": {
        "pin": "P9_22", #Servo1
        "pull_duty": 5,
        "standby_duty": 6.3,
        "push_duty": 7.2
    },
    # Used by collector/sorter
    "orange_piston": {
        "pin": "P9_14", #Servo0
        "pull_duty": 5.5,
        "standby_duty": 6.7,
        "push_duty": 7.7
    },
    # Used by collector/vacuum_shaker
    "vacuum_servo": {
        "pin": "P9_42", #Servo3
        "complete_standby_duty": 8.5,
        "standby_duty": 5.8,
        "pull_duty": 4.0,
        "push_duty": 2.8 #NE PAS DESCENDRE PLUS BAS. Monter PULL_DUTY/COMPLETE_STANDBY_DUTY a la place.
    },
    # Used by collector/collector_controller
    "gate_servo": {
        "pin": "P8_13", #Servo2
        "pull_duty": 6.4,
        "standby_duty": 6.4,
        "push_duty": 7.6
    },
    # Used by collector/sorter
    "color_sensor": {
        "a_pin": "P9_39", #RGB1
        "b_pin": "P9_40",
        "c_pin": "P9_37",
        "black_val": [0.011822222210466861, 0.016111111268401146, 0.024422221928834916],
        "white_val": [0.063355556130409246, 0.065933333486318593, 0.099533332884311682],
        "orange_val": [0.024511111453175544, 0.073822223246097565, 0.079444444179534918],
        "error_tolerance": 0.03
    },
    # Used by collector/collector_controller
    "start_collect_switch": {
        "pin": "P8_16" # In4
    },
    # Used by collector/vacuum_shaker
    "load_tank_switch": {
        "pin": "P8_14" # In3
    },
    # Used by collector/collector_controller
    "collector_foot_up": {
         "pin": "P8_15" # Magnetic In2
    },
    "collector_foot_down": {
         "pin": "P8_11" # Magnetic In1
    },
    # Used by collector/rail
    "stepper_rail": {
        "pin":"GPIO2_6",    # Stepper1 Step
        "direction":"P8_43",# Stepper1 Dir
        "reset":"P8_44",    # Stepper1 Reset
        "enable":"P8_46",   # Stepper1 Enable

        "ramp_step":500,
        'min_sleep':175
    },
     # Used by collector/rail
    "rail": {
        "switch_away": "P8_22", # In7
        "switch_home": "P8_18", # In5
    },

    #Config du pied
    "camion_foot": {
       "stepper_start_position_ticks": 1200,
       "stepper_complete_ticks": 41000/4, #20.5' <- Distance foot to floor
    },
    # Used by camion/camion
    "camion_collector_switch": {
        "pin":"P8_18", # In5
    },
    # Used by camion/camion
    # RF switch
     "camion_rf_switch": {
        "pin":"P8_22", # In7
    },
    # Used by camion/camion
    # Switch below the camion, detect when the foot is up
    "camion_foot_up_switch": {
        "pin":"P8_14", # In3
    },
    # Used by camion/camion
    # Switch above the camion, detect when the foot is down
    "camion_foot_down_switch": {
        "pin":"P8_16", # In4
    },
    # Used by camion/camion when ready to go to init position
    "camion_in_position_switch": {
        "pin":"P8_12", # In2
    },

    "camion_stepper": {
        "pin":"GPIO2_6",    # Stepper1 Step
        "direction":"P8_43",# Stepper1 Dir
        "reset":"P8_44",    # Stepper1 Reset
        "enable":"P8_46",   # Stepper1 Enable
        "ramp_step":2000,
        'min_sleep':120
    },

    # Used by tools/process_spawner. Not used anymore.
    "spawn_switch": {
        "pin": "P8_12" # In2
    }
}
