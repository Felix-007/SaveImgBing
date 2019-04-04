# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import os
import ssl
import re
import time

#如果爬取的网站是https协议的，需要在请求时会验证一次SSL证书
ssl.create_default_context=ssl._create_unverified_context
 
PAGE_URL = 'https://cn.bing.com/'

#step1 获取网页源代码
def getHtml(PAGE_URL):
    page=urllib.request.urlopen(PAGE_URL)
    html=page.read()
    html=html.decode('utf-8')
    return html

#step2 过滤出图片URL
def getImg(html):
    reg='/th.*?;pid=hp"'
    imgre=re.compile(reg)
    imgList=imgre.findall(html)
    return imgList

#step3 定义图片保存路径
def make_dir(floder):
    print(os.getcwd())
    path=os.getcwd()+'/'+floder
    if not os.path.isdir(path):
        os.makedirs(path)
    return path

#stop4 保存图片
def save_img(imgList,path):
    # curt=time.strftime("%Y%m%d%H%M%S")
    curt=time.strftime("%Y%m%d")
    for imgurl in imgList:
        urllib.request.urlretrieve(PAGE_URL+imgurl,'{}/{}.jpg'.format(path,curt))
        # raise TypeError("保存失败")
    return 1




if __name__=='__main__':
    html=getHtml(PAGE_URL)
    print("step1:获取网页源码成功")
    imgList=getImg(html)
    print("#step2 过滤出图片URL")
    print(imgList)
    path=make_dir('bingBKimg')
    print("#step3 定义图片保存路径")
    if(save_img(imgList,path)):
        print("图片爬取保存成功")
        
os.system("pause")
