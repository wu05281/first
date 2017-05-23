#!/usr/local/bin python3
# encoding=utf-8


import os
from PIL import Image

# 图片最大减少的像素值
SQUARE_FIT_SIZE = 800
LOGO_FILE_NAME = 'catlogo.png'

logo_im = Image.open(LOGO_FILE_NAME)
logo_width, logo_height = logo_im.size
print('logo image size:%s,%s' %(logo_width, logo_height))
os.makedirs('img_with_logo', exist_ok=True)
for file_name in os.listdir('.'):
    if not (file_name.endswith('.png') or file_name.endswith('jpg')) or file_name == LOGO_FILE_NAME:
        continue
    im = Image.open(file_name)
    width, height = im.size
    print(width, height)
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int(SQUARE_FIT_SIZE / width * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int(width * SQUARE_FIT_SIZE / height)
            height = SQUARE_FIT_SIZE
        im = im.resize((width, height))
    print('img:%s size, width:%s, height:%s' % (file_name, width, height))
    im.paste(logo_im, (width - logo_width, height - logo_height), logo_im)
    im.save(os.path.join('img_with_logo', file_name))
