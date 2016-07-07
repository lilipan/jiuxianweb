# encoding=utf-8

from requests import get
from lxml import etree
import urllib
import os

f = open("jiuxian.txt", "r")
lines = f.readlines()
i = 0
filename = "jiuxian_pic"
for line in lines:
    j = 0
    url = line.strip()
    print url
    res = get(url)
    text = res.text
    tree = etree.HTML(text)
    node = tree.xpath("//div[@class='show-list-con']/ul[@class='clearfix']//a/img/@src")
    print(len(node))
    for y in range(0, len(node)):
        big = str(node[y]).replace('1.jpg', '5.jpg')
        # print type(node[y])
        if not os.path.exists(filename):
            os.makedirs(filename)
        s = "/{0}-{1}".format(i, j)+".jpg"
        urllib.urlretrieve(big, filename=filename+s)
        j += 1
        # print node[y]
    i += 1


