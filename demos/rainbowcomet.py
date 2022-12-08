import board
import neopixel

from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import (
    PURPLE,
    WHITE,
    AMBER,
    JADE,
    TEAL,
    PINK,
    MAGENTA,
    ORANGE,
)

pixel_pin = board.D10

ORDER = neopixel.GRB

num_pixels = 8

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.05, auto_write=False)
pixels.brightness = 0.5

solid = Solid(pixels, color=PINK)
blink = Blink(pixels, speed=0.5, color=JADE)
colorcycle = ColorCycle(pixels, speed=0.4, colors=[MAGENTA, ORANGE, TEAL])
chase = Chase(pixels, speed=0.1, color=JADE, size=3, spacing=6)
comet = Comet(pixels, speed=0.75, color=PURPLE, tail_length=10, bounce=True)
pulse = Pulse(pixels, speed=0.1, color=AMBER, period=3)


animations = AnimationSequence(
    comet, pulse, chase, advance_interval=5, auto_clear=True, random_order=True
)

rainbow_comet = RainbowComet(pixels, speed=0.1, tail_length=7, bounce=True)

while True:
    rainbow_comet.animate()