#!/usr/bin/env python3
# -*- utf8 -*-
from PIL import Image
import hashlib
import time
from vector_compare import VectorCompare
import os
im = Image.open('python_captcha/captcha.gif')
im.convert('P')
values = {}
his = im.histogram()
for i in range(256):
    values[i] = his[i]
# highest 10 colors used
# for j,k in sorted(values.items(),key=lambda x:x[1],reverse=True)[:10]:
#     print(j,k)
# 220=Red 227=gray
im2 = Image.new("P", im.size, 255)

# height
for x in range(im.size[1]):
    # width
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        if pix == 220 or pix == 227:

            im2.putpixel((y, x), 0)
            # print(8,end="")
    #     else:
    #         print(' ',end="")
    # print(' ')
# this line don't have a perform. use print instead
# im2.show()
# split each character, in this example just cut it
inletter = False
foundletter = False
start = 0
end = 0
letters = []
for y in range(im2.size[0]):
    # scan columns by columns, start at the character first column, end at a empty column
    # this method fails at when character have no empty column between each other
    for x in range(im2.size[1]):
        pix = im2.getpixel((y, x))
        if pix != 255:
            inletter = True
    if foundletter == False and inletter == True:
        foundletter = True
        start = y
    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start, end))
    inletter = False

count = 0
for letter in letters:
    m = hashlib.md5()
    # cut a rectangle from left top to right bottom
    im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
    m.update("{}{}".format(time.time(), count).encode('utf8'))
    im3.save("./{}.gif".format(m.hexdigest()))
    count += 1


def buildvector(im):
    dl = {}
    count = 0
    for i in im.getdata():
        dl[count] = i
        count += 1
    return dl


v = VectorCompare()
iconset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
imageset = []
for letter in iconset:
    for img in os.listdir('./python_captcha/iconset/{}/'.format(letter)):
        temp = []
        if img != "Thumbs.db" and img != ".DS_Store":
            temp.append(buildvector(Image.open(
                "./python_captcha/iconset/{}/{}".format(letter, img))))
        imageset.append({letter: temp})
count=0
for letter in letters:
    m=hashlib.md5()
    im3=im2.crop((letter[0], 0, letter[1], im2.size[1]))
    guess=[]
    for image in imageset:
        # print(image)
        # exit()
        for x,y in image.items():
            if len(y)!=0:
                guess.append((v.relation(y[0],buildvector(im3)),x))
    guess.sort(reverse=True)
    print("",guess[0])
    count+=1
