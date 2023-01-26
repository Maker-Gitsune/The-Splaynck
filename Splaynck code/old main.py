#This is set up for Colmak-DH with h-digraph chords.
#rename to just "main" before using.

print("starting")

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import simple_key_sequence

keyboard = KMKKeyboard()

# Adding extensions
modtap = ModTap()
layers_ext = Layers()
combos = Combos()
MouseKeys = MouseKeys()
MediaKeys = MediaKeys()

keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)
keyboard.modules.append(combos)
keyboard.modules.append(MouseKeys)
keyboard.modules.append(MouseKeys)

# tap time - duration of keystroke
KDur = 100

# Cleaner key names

copy = simple_key_sequence(
	(
        KC.LCTL(KC.C),
	)
)

paste = simple_key_sequence(
	(
        KC.LCTL(KC.V),
	)
)

cut = simple_key_sequence(
	(
        KC.LCTL(KC.X),
	)
)

bgrm_ch = simple_key_sequence(
	(
        KC.C,
        KC.H,
	)
)

bgrm_ph = simple_key_sequence(
	(
        KC.P,
        KC.H,
	)
)

bgrm_sh = simple_key_sequence(
	(
        KC.S,
        KC.H,
	)
)

bgrm_th = simple_key_sequence(
	(
        KC.T,
        KC.H,
	)
)

bgrm_wh = simple_key_sequence(
	(
        KC.W,
        KC.H,
	)
)

bgrm_gh = simple_key_sequence(
	(
        KC.G,
        KC.H,
	)
)

bgrm_qu = simple_key_sequence(
	(
        KC.Q,
        KC.U,
	)
)
______ = KC.TRNS
XXXXXX = KC.NO
MSB_l = KC.MB_LMB
MSB_r = KC.MB_RMB
MSW_up = KC.MW_UP
MSW_dn = KC.MW_DN

LOWER = KC.LT(2, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=KDur)
RAISE = KC.LT(1, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=KDur)
IDK = KC.CAPS # KC.TG(5)
LSFT_S = KC.LT(3, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=KDur)
RSFT_S = KC.MT(KC.SPC, KC.RSFT, prefer_hold=True, tap_interrupted=False, tap_time=150)
ctrl_t = KC.MT(KC.TAB, KC.LCTL, prefer_hold=True, tap_interrupted=False, tap_time=KDur)
ctrl_a = KC.MT(KC.QUOT, KC.LCTL, prefer_hold=True, tap_interrupted=False, tap_time=KDur)
# Combo/sequence stuff
combos.combos = [
    Chord((RAISE, LOWER), KC.MO(4)),
    Chord((KC.COMM, KC.DOT), KC.COLN),
    Chord((KC.DOT, KC.SLSH), KC.SCLN),
    Chord((KC.C, KC.D), bgrm_ch),
    Chord((KC.F, KC.P), bgrm_ph),
    Chord((LSFT_S, KC.S), bgrm_sh),
    Chord((LSFT_S, KC.T), bgrm_th),
    Chord((KC.F, KC.W), bgrm_wh),
    Chord((KC.G, KC.T), bgrm_gh),
    Chord((LSFT_S, bgrm_qu), KC.Q),
    Chord((KC.LCTL, KC.RCTL), KC.TG(5)),
    Chord((LSFT_S, KC.E), KC.Q),

]


keyboard.keymap = [
    [  # colemak
         KC.ESC, bgrm_qu,     KC.W,     KC.F,     KC.P,     KC.B,    KC.J,    KC.L,     KC.U,     KC.Y,  KC.SCLN,           KC.ENTER,
         ctrl_t,    KC.A,     KC.R,     KC.S,     KC.T,     KC.G,             KC.M,     KC.N,     KC.E,     KC.I,     KC.O,   ctrl_a,
        KC.LCTL,    KC.Z,     KC.X,     KC.C,     KC.D,     KC.V,     IDK,    KC.K,     KC.H,  KC.COMM,   KC.DOT,  KC.SLSH,  KC.RCTL,
                           KC.LGUI,  KC.LALT,    LOWER,   LSFT_S,  RSFT_S,   RAISE,  KC.RALT,  KC.RGUI,
    ],
    [  # LOWER
         KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,   KC.F7,   KC.F8,    KC.F9,    KC.F10,  KC.F11,             KC.F12,
        ctrl_t,    KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,            KC.N6,    KC.N7,     KC.N8,   KC.N9,    KC.N0,   ctrl_a,
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
         XXXXXX,  XXXXXX,      cut,     copy,    paste,   XXXXXX,  XXXXXX, KC.HOME,  KC.PGUP,  KC.PGDN,   KC.END,             XXXXXX,
         KC.TAB, KC.LGUI,  KC.LALT,  KC.LCTL,  KC.LSFT,   XXXXXX,           MSW_up,  KC.LEFT,    KC.UP,  KC.DOWN, KC.RIGHT,   XXXXXX,
         XXXXXX,  XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,  XXXXXX,  MSW_dn,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,
                            XXXXXX,   XXXXXX,   XXXXXX,   LSFT_S,   MSB_l,   MSB_r,   XXXXXX,   XXXXXX,
    ],
    [  # system
         XXXXXX,  XXXXXX,  KC.BRID,  KC.BRIU,   XXXXXX,   XXXXXX, KC.MUTE,  KC.VOLD, KC.VOLU,   XXXXXX,   XXXXXX,             XXXXXX,
         XXXXXX,  XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,            XXXXXX,  XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,
         XXXXXX,  XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,  XXXXXX,   XXXXXX,  XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,   XXXXXX,
                            XXXXXX,   XXXXXX,    LOWER,   XXXXXX,  XXXXXX,    RAISE,  XXXXXX,   XXXXXX,
    ],
    
]

if __name__ == '__main__':
    keyboard.go()
# Write your code here :-)
