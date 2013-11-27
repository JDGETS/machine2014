devices = {
    "vacuum": {
        "pin": "P0_00"
    },
    "white_piston": {
        "pin": "P9_14",
        "pull_duty": 9.4,
        "standby_duty": 10.5,
        "push_duty": 11.5
    },
    "orange_piston": {
        "pin": "P9_22"
        "pull_duty": 5.5,
        "standby_duty": 7,
        "push_duty": 7.7
    },
    "color_sensor": {
        "r_pin": "P9_33",
        "g_pin": "P9_35",
        "b_pin": "P9_36",
        "white_val": [255,255,255],
        "orange_val": [255, 255, 0],
        "error": 128
    }
}

