#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
from lxml import etree


def loadPage(url):
    """
        作用：根据url发送请求，获取服务器响应文件
        url: 需要爬取的url地址
    """
    # print url
    # headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}

    request = urllib2.Request(url)
    html = urllib2.urlopen(request).read()
    # 解析HTML文档为HTML DOM模型
    content = etree.HTML(html)
    # print content
    # 返回所有匹配成功的列表集合
    link_list = content.xpath('//span/img/@data-original')
    for link in  link_list:
        link="http://"+link[2:]
        writeImage(link)
def writeImage(link):
    """
        作用：将html内容写入到本地
        link：图片连接
    """
    # print "正在保存 " + filename
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    # 文件写入
    request = urllib2.Request(link, headers=headers)
    # 图片原始数据
    image = urllib2.urlopen(request).read()
    # 取出连接后10位做为文件名
    filename = link[-20:]
    # 写入到本地磁盘文件内
    with open(filename, "wb") as f:
        f.write(image)
    print "已经成功下载 " + filename


def tiebaSpider(url):
        loadPage(url)



if __name__ == "__main__":

    url = "http://www.huya.com/g/2168"
    tiebaSpider(url)
