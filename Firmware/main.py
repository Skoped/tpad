import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

#--key matrix--
keyboard.col_pins = (board.GP5, board.GP4, board.GP3)
keyboard.row_pins = (board.GP7, board.GP6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#--modules for layers and rotary encoders--
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

encoder_handler.pins = (
    (board.GP9, board.GP10, board.GP11),
)

#--extensions for media keys and oled--
keyboard.extensions.append(MediaKeys())

i2c = busio.I2C(scl=board.GP2, sda=board.GP1)
display_driver = SSD1306(i2c=i2c, device_address=0x3C)

display = Display(
    display=display_driver,
    width=128,
    height=32,
    entries=[
        TextEntry(text='Layer 0', x=4, y=16, y_anchor='M', layer=0),
        TextEntry(text='Layer 1', x=4, y=16, y_anchor='M', layer=1)
    ],
)
keyboard.extensions.append(display)

#--keymap--
keyboard.keymap = [
     #layer0 keymap before pressing key 6
        [KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.MO(1)],
        [KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.TRNS],
]

#--rotary encoder stuff--
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.TG(1)),), #when knob isnt not held
    ((KC.BRID, KC.BRIU, KC.TRNS),), #when knob is held
]

if __name__ == '__main__':
    keyboard.go()