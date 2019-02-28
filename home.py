#   Pil和Pillow不能同时存在,使用的是Pillow模块
from PIL import Image, ImageFont, ImageDraw

#   获取图片
im = Image.open("999.png")

#   获取字体和字号值
myfont = ImageFont.truetype("C:/windows/fonts/Arial.ttf", size=55)

#   使用此模块创建新图像
draw = ImageDraw.Draw(im)

#   写入坐标，内容，字色，变量
draw.text((446, 906), "Hello World",  fill=(251, 198, 0), font= myfont)

#   显示此图像。此方法主要用于调试目的。
im.show()

#   输出图片
im.save('new.png')