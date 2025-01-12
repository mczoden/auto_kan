"""Game GUI"""
game_gui = {
    # Poi on Dell laptop screen ?
    # 'offset_x': 0,
    # 'offset_y': 141,

    # Poi on Dell laptop screen ?
    'offset_x': 0,
    'offset_y': 75,

    # Edge on Lenovo LCD
    # 'offset_x': 312,
    # 'offset_y': 135,

    # Firefox Lenovo LCD
    # 'offset_x': 311,
    # 'offset_y': 136,

    # Edge on Dell P2417H
    # 'offset_x': 480,
    # 'offset_y': 135,

    # Firefox on Dell P2417H without vertical scroll
    # 'offset_x': 480,
    # 'offset_y': 136,

    # Firefox on Dell P2417H with vertical scroll
    # 'offset_x': 471,
    # 'offset_y': 136,
    'window': {
        # Lost right 1 pixel
        'shape': 'rectangle',
        'x': 480,
        'y': 287,
        'radius_x': 480,
        'radius_y': 287
    },
    'port': {
        'shape': 'rectangle',
        'x': 55,
        'y': 55,
        'radius_x': 45,
        'radius_y': 45
    },
    'port_confirm_areas': [{
        'shape': 'dot',
        'x': 940,
        'y': 536,
        'color_match_func':
            lambda r, g, b: r < 20 and 150 < g < 170 and 150 < b < 170
    }, {
        'shape': 'dot',
        'x': 926,
        'y': 543,
        'color_match_func':
            lambda r, g, b: r > 240 and g > 240 and b > 240
    }],
    'sortie_in_port': {
        'shape': 'circle',
        'x': 235,
        'y': 314,
        'radius': 40
    },
    'sortie_main_confirm_areas': [{
        'shape': 'dot',
        'x': 228,
        'y': 346,
        'color_match_func': lambda r, g, b: r > 240 and g > 240 and b > 240
    }],
    'organize_in_port': {},
    'supply_in_port': {
        'shape': 'circle',
        'x': 90,
        'y': 260,
        'radius': 40
    },
    'supply_main_confirm_areas': [{
        'shape': 'dot',
        'x': 780,
        'y': 250,
        'color_match_func':
            lambda r, g, b: 235 < r < 255 and 220 < g < 240 and 180 < b < 200
    }, {
        'shape': 'dot',
        'x': 900,
        'y': 250,
        'color_match_func':
            lambda r, g, b: 225 < r < 235 and 180 < g < 190 and 165 < b < 175
    }],
    'refit_in_port': {},
    'docking_in_port': {},
    'factory_in_port': {},
    'organize_in_submenu': {
        'shape': 'rectangle',
        'x': 25,
        'y': 185,
        'radius_x': 10,
        'radius_y': 15
    },
    'supply_in_submenu': {
        'shape': 'rectangle',
        'x': 25,
        'y': 250,
        'radius_x': 10,
        'radius_y': 15
    },
    'refit_in_submenu': {
        'shape': 'rectangle',
        'x': 25,
        'y': 315,
        'radius_x': 10,
        'radius_y': 15
    },
    'docking': {
        'shape': 'rectangle',
        'x': 25,
        'y': 380,
        'radius_x': 10,
        'radius_y': 15
    },
    'port_in_submenu': {
        'shape': 'rectangle',
        'x': 88,
        'y': 310,
        'radius_x': 12,
        'radius_y': 20
    },
    'sortie_in_sortie': {
        'shape': 'circle',
        'x': 270,
        'y': 270,
        'radius': 100
    },
    'practice_in_sortie': {
        'shape': 'circle',
        'x': 540,
        'y': 270,
        'radius': 100
    },
    'expedition_in_sortie': {
        'shape': 'circle',
        'x': 800,
        'y': 270,
        'radius': 100
    },
    'expedition_in_sortie_confirm_areas': [{
        'shape': 'dot',
        'x': 853,
        'y': 477,
        'color_match_func': lambda r, g, b: r > 230 and g > 230 and b > 210
    }],
    'map1_in_expedition': {
        'shape': 'rectangle',
        'x': 156,
        'y': 521,
        'radius_x': 22,
        'radius_y': 21
    },
    'map2_in_expedition': {
        # lost right 1 pixel
        'shape': 'rectangle',
        'x': 205,
        'y': 521,
        'radius_x': 21,
        'radius_y': 21
    },
    'map3_in_expedition': {
        'shape': 'rectangle',
        'x': 255,
        'y': 521,
        'radius_x': 22,
        'radius_y': 21
    },
    'map4_in_expedition': {
        'shape': 'rectangle',
        'x': 305,
        'y': 521,
        'radius_x': 22,
        'radius_y': 21
    },
    'map5_in_expedition': {
        # lost right 1 pixel
        'shape': 'rectangle',
        'x': 354,
        'y': 521,
        'radius_x': 21,
        'radius_y': 21
    },
    'map6_in_expedition': {
        # to skip "NEXT" down arrow
        'shape': 'rectangle',
        'x': 411,
        'y': 521,
        'radius_x': 15,
        'radius_y': 21
    },
    'map7_in_expedition': {
        # lost right 1 pixel
        'shape': 'rectangle',
        'x': 453,
        'y': 521,
        'radius_x': 21,
        'radius_y': 21
    },
    'bottom_map_select_area': {
        'shape': 'rectangle',
        'x': 304.5,
        'y': 521,
        'radius_x': 170.5,
        'radius_y': 22
    },
    'expedition_height': 36,
    'expedition_radius_x': 260,
    'expedition_border': 1,  # not used
    'expedition_center_x': 397,
    'expedition_left_x': 137,
    'expedition_right_x': 657,
    # expedition bar in 80% scale is not symmetry in vertical
    # use base + height algorithm instead of center + radius
    '1st_expedition_center_y': 207,
    '1st_expedition_base_y': 190,
    'human_select_expedition_from_right_center_x': 470,
    'human_select_expedition_from_right_radius_x': 150,
    'human_select_expedition_from_bottom_radius_x': 75,
    'human_select_expedition_from_current_radius_x': 150,
    'human_select_expedition_all_range_probability': 20,
    'confirm_expedition': {
        # Lost 1 pixel at bottom
        'shape': 'rectangle',
        'x': 823,
        'y': 533,
        'radius_x': 115,
        'radius_y': 23
    },
    'start_expedition': {
        # Lost 1 pixel at bottom
        'shape': 'rectangle',
        'x': 736,
        'y': 533,
        # 'radius_x': 100,
        'radius_x': 98,
        'radius_y': 21
    },
    'start_expedition_confirm_areas': [{
        'shape': 'dot',
        'x': 689,
        'y': 238,
        'color_match_func':
            lambda r, g, b: 40 < r < 60 and 40 < g < 60 and 40 < b < 60
    }, {
        'shape': 'dot',
        'x': 850,
        'y': 238,
        'color_match_func':
            lambda r, g, b: 40 < r < 60 and 40 < g < 60 and 40 < b < 60
    }, {
        'shape': 'dot',
        'x': 766,
        'y': 459,
        'color_match_func':
            lambda r, g, b: 40 < r < 60 and 40 < g < 60 and 40 < b < 60
    }],
    'no_expedition_is_leaving_confirm_areas': [{
        'shape': 'dot',
        'x': 370,
        'y': 270,
        'color_match_func':
            lambda r, g, b: r > 100 and g > 100 and b > 100
    }, {
        'shape': 'dot',
        'x': 370,
        'y': 280,
        'color_match_func':
            lambda r, g, b: r > 100 and g > 100 and b > 100
    }, {
        'shape': 'dot',
        'x': 370,
        'y': 290,
        'color_match_func':
            lambda r, g, b: r > 100 and g > 100 and b > 100
    }, {
        'shape': 'dot',
        'x': 900,
        'y': 290,
        'color_match_func':
            lambda r, g, b: r > 100 and g > 100 and b > 100
    }, {
        'shape': 'dot',
        'x': 130,
        'y': 290,
        'color_match_func':
            lambda r, g, b: r > 100 and g > 100 and b > 100
    }],
    'select_expedition_fleet2': {
        # lost 1 pixel top
        'shape': 'rectangle',
        'x': 468,
        'y': 137,
        'radius_x': 13,
        'radius_y': 11
    },
    'select_expedition_fleet3': {
        # lost 1 pixel top
        'shape': 'rectangle',
        'x': 504,
        'y': 137,
        'radius_x': 13,
        'radius_y': 11
    },
    'select_expedition_fleet4': {
        # lost 1 pixel top
        'shape': 'rectangle',
        'x': 539,
        'y': 137,
        'radius_x': 13,
        'radius_y': 11
    },
    'supply_all_in_supply': {
        # lost 1 pixel bottom
        'shape': 'rectangle',
        'x': 143,
        'y': 143,
        'radius_x': 13,
        'radius_y': 12
    },
    'fleet1_in_supply': {
        # lost 1 pixel top
        'shape': 'rectangle',
        'x': 176,
        'y': 143,
        'radius_x': 10,
        'radius_y': 11
    },
    'fleet2_in_supply': {
        # lost 1 pixel top
        'shape': 'rectangle',
        'x': 212,
        'y': 143,
        'radius_x': 10,
        'radius_y': 11
    },
    'fleet3_in_supply': {
        # lost 1 pixel top
        'shape': 'rectangle',
        'x': 247,
        'y': 143,
        'radius_x': 10,
        'radius_y': 11
    },
    'fleet4_in_supply': {
        'shape': 'rectangle',
        'x': 283,
        'y': 144,
        'radius_x': 10,
        'radius_y': 10
    },
    'supply_fleet1_is_selected_confirm_areas': [{
        'shape': 'dot',
        'x': 184,
        'y': 141,
        'color_match_func':
            lambda r, g, b: 30 < r < 40 and 150 < g < 165 and 155 < b < 165
    }],
    'supply_fleet2_is_selected_confirm_areas': [{
        'shape': 'dot',
        'x': 220,
        'y': 141,
        'color_match_func':
            lambda r, g, b: 30 < r < 40 and 150 < g < 165 and 155 < b < 165
    }],
    'supply_fleet3_is_selected_confirm_areas': [{
        'shape': 'dot',
        'x': 256,
        'y': 141,
        'color_match_func':
            lambda r, g, b: 30 < r < 40 and 150 < g < 165 and 155 < b < 165
    }],
    'supply_fleet4_is_selected_confirm_areas': [{
        'shape': 'dot',
        'x': 292,
        'y': 141,
        'color_match_func':
            lambda r, g, b: 30 < r < 40 and 150 < g < 165 and 155 < b < 165
    }],
    '1st_ship_need_to_supply_confirm_areas': [{
        'shape': 'dot',
        'x': 135,
        'y': 195,
        'color_match_func':
            lambda r, g, b: (r, g, b) == (68, 68, 68)
    }],
    'expedition_flag_confirm_areas': [{
        'shape': 'dot',
        'x': 627,
        'y': 34,
        'color_match_func':
            lambda r, g, b: 40 < r < 50 and 170 < g < 180 and 170 < b < 180
    }],
    'expedition_check': {
        'shape': 'rectangle',
        'x': 479,
        'y': 287,
        'radius_x': 240,
        'radius_y': 140
    },
    'expedition_checked_next_confirm_areas': [{
        'shape': 'dot',
        'x': 897,
        'y': 526,
        'color_match_func':
            lambda r, g, b: 20 < r < 30 and 150 < g < 160 and 150 < b < 160
    }],
    'expedition_fleet2_is_selected_confirm_areas': [{
        'shape': 'dot',
        'x': 477,
        'y': 135,
        'color_match_func':
            lambda r, g, b: 30 < r < 40 and 150 < g < 165 and 155 < b < 165
    }],
    'expedition_fleet3_is_selected_confirm_areas': [{
        'shape': 'dot',
        'x': 513,
        'y': 135,
        'color_match_func':
            lambda r, g, b: 30 < r < 40 and 150 < g < 165 and 155 < b < 165
    }],
    'expedition_fleet4_is_selected_confirm_areas': [{
        'shape': 'dot',
        'x': 549,
        'y': 135,
        'color_match_func':
            lambda r, g, b: 30 < r < 40 and 150 < g < 165 and 155 < b < 165
    }],
    'expedition_result_confirm_areas': [
        {
            'shape': 'dot',
            'x': 200,
            'y': 295,
            'color_match_func':
                lambda r, g, b: r > 250 and g > 250 and b > 250
        }, {
            'shape': 'dot',
            'x': 320,
            'y': 295,
            'color_match_func':
                lambda r, g, b: r > 250 and g > 250 and b > 250
        }
    ]
}
