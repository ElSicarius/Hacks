from PIL import Image, ImageFont, ImageDraw,  ImageEnhance
import textwrap
import sys


import os, glob
from PIL import Image
import uuid

if not os.path.exists("./decoded/"):
    os.mkdir("./decoded/")

if not os.path.exists("./gamma/"):
    os.mkdir("./gamma/")

def image(file_location, r=1):
    print('[+] Opening image '+ file_location)
    encoded_image = Image.open(file_location)
    print('[+] Extracting colors')
    red_channel = encoded_image.split()[0]
    green_channel = encoded_image.split()[1]
    blue_channel = encoded_image.split()[2]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]
    print('[+] Creating images')
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    z = r
    print("[+] Exploiting byte number "+str(z))
    for i in range(x_size):
        for j in range(y_size):
            try:
                a = str(bin(red_channel.getpixel((i, j)))).split("b")[1]
                b = str(bin(green_channel.getpixel((i, j)))).split("b")[1]
                c = str(bin(blue_channel.getpixel((i, j)))).split("b")[1]
                a = f"{a:0>8.9}"
                b = f"{b:0>8.9}"
                c = f"{c:0>8.9}"
                a_ = 0 if a[z] == '0' else 240
                b_ = 0 if b[z] == '0' else 250
                c_ = 0 if c[z] == '1' else 140
                pixels[i, j] = (int(a_/1), int(b_/1), int(c_/1))
            except Exception as e:
                print(e)
    print('[+] Writing image number '+str(z))
    decoded_image.save("./decoded/"+str(uuid.uuid4().hex)+".png")

def gamma(file_loc):
    im = Image.open(file_loc)
    enhancer = ImageEnhance.Brightness(im)
    for i in range(20,1,-1):
        i = i/10
        im_output = enhancer.enhance(i)
        im_output.save("./gamma/"+str(uuid.uuid4().hex)+'.png')

def gray(file_loc):
    im = Image.open(file_loc).convert('LA')
    im.save("./gray/"+str(uuid.uuid4().hex)+".png")



if __name__ == '__main__':
    #extractFrames(sys.argv[1],"decoded/")
    #image( sys.argv[1], r=0)

    gamma(sys.argv[1])
    for img in glob.glob("./gamma/*"):
        image( img, r=0)
    os.popen("rm ./gamma/*")
    for img in glob.glob("./decoded/*"):
        gray( img)
