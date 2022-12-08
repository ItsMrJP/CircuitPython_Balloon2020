# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
NeoPixel example for Pico. Turns the NeoPixels red, green, and blue in sequence.

REQUIRED HARDWARE:
* RGB NeoPixel LEDs connected to pin GP0.
"""
import time
import board
from rainbowio import colorwheel
import neopixel
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.sequence import AnimationSequence

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D10

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 8

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.05, auto_write=False)
pixels.brightness = 0.5

rainbow = Rainbow(pixels, speed=0.1, period=2)
rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3)
rainbow_comet = RainbowComet(pixels, speed=0.1, tail_length=7, bounce=True)
rainbow_sparkle = RainbowSparkle(pixels, speed=0.1, num_sparkles=15)


animations = AnimationSequence(
    rainbow,
    rainbow_chase,
    rainbow_comet,
    rainbow_sparkle,
    advance_interval=5,
    auto_clear=True,
)

while True:
    animations.animate()