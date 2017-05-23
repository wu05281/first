#!/usr/bin/env python3
# encoding=utf-8

from PIL import Image

cat_im = Image.open('zophie.png')
width, height = cat_im.size
print('image file name:%s, format:%s, width:%s, height:%s' % (cat_im.filename, cat_im.format, width, height))

# 创建了一个 Image 对象，它有 100 像素宽、200 像素高，带有紫色 背景
im = Image.new('RGBA', (100, 200), 'purple')
# im.save('purple_img.png')

# new_cat_im = cat_im.resize((int(width/2), int(height/2)))
# new_cat_im.save('new_zophie.png')

# 复制新图像
# cat_copy_im = cat_im.copy()
# face_im = cat_im.crop((335, 345, 565, 560))
# 将另一个图像粘贴在一个图上面
# cat_copy_im.paste(face_im,(0,0))
# cat_copy_im.save('copy_zophie.png')

# 翻转：翻转n度与镜像翻转
# cat_im.rotate(90).save('90_zophie.png')
# cat_im.transpose(Image.FLIP_LEFT_RIGHT).save('transpose_zophie.png')
