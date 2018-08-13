#-*- coding:gb2312 -*-
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random
import re


def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        #print(path + ' 目录已存在')
        return False

def createPic(fontRoute,fontSize):
    # 生成图片
    width = fontSize
    height = fontSize
    im = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建字体
    font = ImageFont.truetype(str(fontRoute), fontSize)
    # 生成绘画对象
    im_draw = ImageDraw.Draw(im)

    # 加上字符
    text_1=open("1.txt")

    text_1=text_1.readlines()

    for i in range(len(text_1)):
        text_1[i]=re.findall(u"[\u4e00-\u9fa5]",str(text_1[i]))
        for j in range(len(text_1[i])):
            #print(text_1[i][j])
            im_draw.text((0, 0), text_1[i][j], font=font, fill=("black"))
            mkdir((".\im\{}").format(str(fontSize)))
            im.save(('.\im\{}\{}.jpg').format(str(fontSize),str(text_1[i][j])), 'JPEG')
            im_draw.rectangle((0,0,100,100),fill=(255,255,255))
            #im.show()


# im = im.filter(ImageFilter.BLUR)

if __name__=="__main__":
    createPic("C:\Windows\Fonts\simsun.ttc",50)
