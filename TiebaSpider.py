# coding:utf-8
import urllib
import urllib2
import random
from xml import etree


# 分配请求
def loaderpage(url):
    header = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50"}
    request = urllib2.Request(url, headers=header)
    return urllib2.urlopen(request).read()


# 写入文件
def writePage(filename, html):
    with open(filename, "w") as f:
        f.write(html)
        print (filename + "写完了")


# 分页请求然后写入
def loader(wd, url, pageStart, pageEnd):
    for page in range(pageStart, pageEnd + 1):
        url = url + "&pn=" + str((page - 1) * 50)
        html = loaderpage(url)
        filename = wd + "吧第" + str(page) + "页.html"
        writePage(filename, html)


if __name__ == "__main__":
    url = "https://tieba.baidu.com/f"
    wd = raw_input("请输入贴吧名称：")
    pageStart = int(raw_input("请输入开始页："))
    pageEnd = int(raw_input("请输入结束页："))
    fullurl = url + urllib.urlencode({"kw": wd})
    loader(wd, fullurl, pageStart, pageEnd)
