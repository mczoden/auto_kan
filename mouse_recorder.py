import sys
import time

import pyautogui as gui
from game_gui import game_gui


def mouse_recorder():
    while True:
        time.sleep(1)
        x, y = gui.position()
        print('position {} no offset {} color {}'.format(
            (x, y),
            (x - game_gui['offset_x'], y - game_gui['offset_y']),
            gui.pixel(x, y)))


def main():
    if len(sys.argv) == 1:
        mouse_recorder()
        return

    if sys.argv[1] == 'fmo' and sys.argv[2].isdigit() and sys.argv[3].isdigit():
        gui.moveTo(int(sys.argv[2]) + game_gui['offset_x'],
                   int(sys.argv[3]) + game_gui['offset_y'])
        return
    
    if sys.argv[1] == 'fm' and sys.argv[2].isdigit() and sys.argv[3].isdigit():
        gui.moveTo(int(sys.argv[2]), int(sys.argv[3]))
        return

    if sys.argv[1] == 'fpo' and sys.argv[2].isdigit() and sys.argv[3].isdigit():
        print(gui.pixel(int(sys.argv[2]) + game_gui['offset_x'],
                        int(sys.argv[3]) + game_gui['offset_y']))
        return


if __name__ == '__main__':
    main()
