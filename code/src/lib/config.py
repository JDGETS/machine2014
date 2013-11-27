devices = {
    "vacuum": {
        "pin": "P0_00"
    },
    "white_piston": {
        "pin": "P9_22",
        "pull_duty": 9.4,
        "standby_duty": 10.5,
        "push_duty": 11.5
    },
    "orange_piston": {
        "pin": "P9_14",
        "pull_duty": 5.5,
        "standby_duty": 7,
        "push_duty": 7.7
    },
    "color_sensor": {
        "a_pin": "P9_33",
        "b_pin": "P9_35",
        "c_pin": "P9_36",
        "black_val": [0.023,0.016,0.030],
        "white_val": [0.075,0.075,0.11],
        "orange_val": [0.088,0.035,0.095],
        "error": 0.02
    }
}

