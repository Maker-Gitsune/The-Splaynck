import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
        board.GP8,
        board.GP9,
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP14,
    )
    row_pins = (
        board.GP21,
        board.GP20,
        board.GP19,
        board.GP18,
    )
    diode_orientation = DiodeOrientation.COLUMNS

    coord_mapping = [
     0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10,     12,
    13, 14, 15, 16, 17, 18,     20, 21, 22, 23, 24, 25,
    26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
            41, 42, 43, 44, 45, 46, 47, 48,
    ]
