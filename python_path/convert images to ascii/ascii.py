#!/usr/bin/env python3
# -*- coding:utf8 -*-
from PIL import Image
import argparse
ascii_char = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
RATIO_R = 0.2126
RATIO_G = 0.7152
RATIO_B = 0.0722


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(RATIO_R*r + RATIO_G*g+RATIO_B*b)
    # unit means: how many gray count equals a move of ascii_char
    unit = (256.0+1)/length

    return ascii_char[int(gray/unit)]


parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)
args = parser.parse_args()

# config consts
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    print(txt)

    if not OUTPUT:
        OUTPUT = 'output.txt'

    with open(OUTPUT, 'w') as f:
        f.write(txt)
