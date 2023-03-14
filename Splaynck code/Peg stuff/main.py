from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)
keyboard.modules = [layers_ext, modtap]
# keymap
keyboard.keymap = [ [KC.ESCAPE,KC.Y,KC.P,KC.O,KC.U,KC.J,KC.K,KC.D,KC.L,KC.C,KC.W,KC.ENTER,KC.TAB,KC.I,KC.N,KC.E,KC.A,KC.COMMA,KC.M,KC.H,KC.T,KC.S,KC.R,KC.TAB,KC.CAPSLOCK,KC.Q,KC.Z,KC.SLASH,KC.DOT,KC.SCOLON,KC.F5,KC.B,KC.F,KC.G,KC.V,KC.X,KC.NO,KC.LGUI,KC.LALT,KC.DELETE,KC.RSHIFT,KC.SPC,KC.BSPC,KC.RALT,KC.RGUI], 
[], 
[], 
[], 
[], 
[], 
[], 
[] ] 
# keymap
if __name__ == '__main__': 
    keyboard.go(hid_type=HIDModes.USB)
