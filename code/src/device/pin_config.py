__pin_config = {
    "vacuum": "P0_00",
    "orange_piston": "P0_00",
    "white_piston": "P0_00",
    "color_sensor": "P0_00"
}

def pin_from_id(id):
    global __pin_config
    return __pin_config[id]