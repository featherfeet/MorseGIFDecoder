#!/usr/bin/env python3

from PIL import Image
import sys

if len(sys.argv) != 2:
    print("Usage: ./decoder.py image.gif")
    sys.exit(-1)

img = Image.open(sys.argv[1])
frame = 1

img.seek(img.tell() + 1)

try:
    while True:
        rgb_img = img.convert("RGB")
        color = rgb_img.getpixel((362, 67))
        duration = img.info["duration"]
        if color == (254, 254, 254):
            state = "on"
        elif color == (58, 54, 56):
            state = "off"
        if state == "on" and duration == 200:
            print('.', end = '')
        elif state == "on" and duration == 500:
            print('-', end = '')
        elif state == "off" and duration == 500:
            print(' ', end = '')
        elif state == "off" and duration == 1500:
            print('/', end = '')
        img.seek(img.tell() + 1)
        frame += 1
except EOFError:
    print("")
