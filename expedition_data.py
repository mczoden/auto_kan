"""Expedition Data"""
HOUR = 60 * 60
MINUTE = 60
TIME_UNKNOWN = 0


expedition_data: dict[str, dict[str, int]] = {
    '01': {
        'map': 1,
        'index': 1,
        'time': 15 * MINUTE
    },
    '02': {
        'map': 1,
        'index': 2,
        'time': 30 * MINUTE
    },
    '03': {
        'map': 1,
        'index': 3,
        'time': 20 * MINUTE
    },
    '04': {
        'map': 1,
        'index': 4,
        'time': TIME_UNKNOWN
    },
    '05': {
        'map': 1,
        'index': 5,
        'time': 90 * MINUTE
    },
    '06': {
        'map': 1,
        'index': 6,
        'time': 40 * MINUTE
    },
    '07': {
        'map': 1,
        'index': 7,
        'time': TIME_UNKNOWN
    },
    '08': {
        'map': 1,
        'index': 8,
        'time': TIME_UNKNOWN
    },
    '09': {
        'map': 2,
        'index': 1
    },
    '11': {
        'map': 2,
        'index': 3,
        'time': 5 * HOUR
    },
    '13': {
        'map': 2,
        'index': 5,
        'time': 4 * HOUR
    },
    '17': {
        'map': 3,
        'index': 1,
        'time': 45 * MINUTE
    },
    '21': {
        'map': 3,
        'index': 5,
        'time': 2 * HOUR + 20 * MINUTE
    },
    '37': {
        'map': 6,
        'index': 5,
        'time': 2 * HOUR + 45 * MINUTE
    },
    '38': {
        'map': 6,
        'index': 6,
        'time': 2 * HOUR + 55 * MINUTE
    }
}
