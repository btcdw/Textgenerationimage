#   Pil和Pillow不能同时存在,下面使用的是Pillow模块.
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

#   自动换行模块
import textwrap
#   文本样式
import pandas as pd
#   图片编辑模块
import time
#   时间模块


def Excel_num(a):
    #   获取表格数据
    num = pd.read_excel("a.xls")
    #   读取表格
    text_name = num.iloc[a, 0]
    #   获取2,A数据
    text_title = num.iloc[a, 1]
    #   获取2，B数据
    return text_name, text_title
    #   返回给韩式
    #   print(excel_num())
    #   输出函数里面的内容


def Image_io(text_name, text_title):
    im = Image.open("old.png")
    #   获取图片
    myfont = ImageFont.truetype("a.ttf", size=70)
    myfont2 = ImageFont.truetype("a.ttf", size=50)
    #   获取字体和设置字号大小
    draw = ImageDraw.Draw(im)
    #   使用此模块创建新图像
    draw.text((184, 480), textwrap.fill(text_name.ljust(1), width=400),  fill=(183, 68, 72), font=myfont)
    draw.text((184, 600), textwrap.fill(text_title.rjust(1), width=400), fill=(0, 0, 0), font=myfont2)
    #   写入坐标，换行，内容，字色，变量
    #   ljust(),center(),rjust()函数实现输出的字符串左对齐、居中、右对齐，参数默认空格，10就是10个为一套居中
    im.show()
    #   显示此图像。此方法主要用于调试目的！
    im.save(text_name + ".png")
    #   输出图片到根目录为png格式


if __name__ == '__main__':
    for a in range(0, 5):
        #   创建一个整数列表更具Excel的数量来设置
        text_name, text_title = Excel_num(a)
        #   调用Excel_num(a)方法的返回值赋值给text_name, text_title
        #   print(text_name, text_title)
        Image_io(text_name, text_title)
        #   调用Image_io 将Excel_num(a)的值传入Image_io
        time.sleep(2)
        #   设置循环暂停2秒