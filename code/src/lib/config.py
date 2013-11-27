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
        "black_val": [0.020,0.180,0.027],
        "white_val": [0.078,0.230,0.12],
        "orange_val": [0.077,0.22,0.085],
        "error": 0.02
    }
}

