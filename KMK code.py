print("Starting KMK - XIAO RP2040 4x4 example")

import board
import neopixel

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3)
keyboard.row_pins = (board.GP4, board.GP5, board.GP6, board.GP7)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.F1, KC.F2, KC.F3, KC.F4],
    [KC.Q, KC.W, KC.E, KC.R],
    [KC.A, KC.S, KC.D, KC.F],
    [KC.Z, KC.X, KC.C, KC.V],
]

NEOPIXEL_PIN = board.GP10
NUM_PIXELS = 16 
BRIGHTNESS = 0.12

pixels = neopixel.NeoPixel(NEOPIXEL_PIN, NUM_PIXELS, brightness=BRIGHTNESS, auto_write=True)

pixels.fill((0, 0, 100))

if __name__ == '__main__':
    keyboard.go()