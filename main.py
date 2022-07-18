print("starting")

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# Adding extensions
modtap = ModTap()
layers_ext = Layers()
combos = Combos()
MouseKeys = MouseKeys()
MediaKeys = MediaKeys()

keyboard.modules = [layers_ext, modtap, combos, MouseKeys, MediaKeys]

# Cleaner key names
______ = KC.TRNS
XXXXXX = KC.NO
MSB_l = KC.MB_LMB
MSB_r = KC.MB_RMB
MSW_up = KC.MW_UP
MSW_dn = KC.MW_DN

LOWER = KC.LT(1, KC.DEL)
RAISE = KC.LT(2, KC.BSPC)
IDK = KC.NO # KC.TG(5)
LSFT_S = KC.LT(3, KC.SPC)
RSFT_S = KC.MT(KC.SPC, KC.RSFT)

# Combo stuff
combos.combos = [
    Chord((LSFT_S, RSFT_S), KC.CAPS)
]

combos.combos = [
    Chord((RAISE, LOWER), KC.MO(4))
]

keyboard.keymap = [
    [  # colemak
         KC.ESC,    KC.Q,     KC.W,     KC.F,     KC.P,     KC.B,    KC.J,    KC.L,     KC.U,     KC.Y,  KC.SCLN,           KC.ENTER,
         KC.TAB,    KC.A,     KC.R,     KC.S,     KC.T,     KC.G,             KC.M,     KC.N,     KC.E,     KC.I,     KC.O,  KC.QUOT,
        KC.LCTL,    KC.Z,     KC.X,     KC.C,     KC.D,     KC.V,     IDK,    KC.K,     KC.H,  KC.COMM,   KC.DOT,  KC.SLSH,  KC.RCTL,
                           KC.LGUI,  KC.LALT,    LOWER,   LSFT_S,  RSFT_S,   RAISE,  KC.RALT,  KC.RGUI,
    ],
    [  # LOWER
         KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,   KC.F7,   KC.F8,    KC.F9,    KC.F10,  KC.F11,             KC.F12,
        XXXXXX,    KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,            KC.N6,    KC.N7,     KC.N8,   KC.N9,    KC.N0,   XXXXXX,
       KC.LCTL,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,     IDK,  XXXXXX,   XXXXXX,    XXXXXX,  XXXXXX,   XXXXXX,  KC.RCTL,
                           KC.LGUI,  KC.LALT,    LOWER,   LSFT_S,  RSFT_S,   RAISE,  KC.RALT,   KC.RGUI,
    ],
    [  # RAISE
         KC.ESC,  XXXXXX,  KC.UNDS,  KC.MINS,  KC.LPRN,   XXXXXX,  XXXXXX, KC.RPRN,  KC.PPLS,   KC.EQL,   XXXXXX,           KC.ENTER,
         KC.TAB, KC.EXLM,    KC.AT,  KC.HASH,   KC.DLR,  KC.PERC, KC.CIRC,           KC.AMPR,  KC.ASTR,  KC.LPRN,  KC.RPRN,  KC.QUOT,
        KC.LCTL,  KC.GRV,  KC.TILD,   XXXXXX,  KC.LBRC,  KC.LCBR,     IDK, KC.RCBR,  KC.RBRC,   XXXXXX,  KC.BSLS,  KC.PIPE,  KC.RCTL,
                           KC.LGUI,  KC.LALT,    LOWER,   LSFT_S,  RSFT_S,   RAISE,  KC.RALT,  KC.RGUI,
    ],
    [  # EXTEND
         XXXXXX,  XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,  XXXXXX, KC.HOME,  KC.PGUP,  KC.PGDN,   KC.END,             XXXXXX,
         KC.TAB, KC.LGUI,  KC.LALT,  KC.LCTL,  KC.LSFT,   XXXXXX,           MSW_up, KC.MS_LT, KC.MS_UP, KC.MS_DN, KC.MS_RT,   XXXXXX,
         XXXXXX,  XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,  XXXXXX,  MSW_dn,  KC.LEFT,    KC.UP,  KC.DOWN, KC.RIGHT,   XXXXXX,
                            XXXXXX,   XXXXXX,   XXXXXX,   LSFT_S,   MSB_l,   MSB_r,   XXXXXX,   XXXXXX,
    ],
    [  # system
         XXXXXX,  XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,  XXXXXX, KC.VOLD,  KC.VOLU,   XXXXXX,   XXXXXX,             XXXXXX,
         XXXXXX,  XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,            XXXXXX,  XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,
         XXXXXX,  XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,  XXXXXX,   XXXXXX,  XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,
                            XXXXXX,   XXXXXX,    LOWER,   XXXXXX,  XXXXXX,   RAISE,   XXXXXX,   XXXXXX,
    ],
]

if __name__ == '__main__':
    keyboard.go()
