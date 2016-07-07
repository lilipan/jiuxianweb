# -*- coding: utf-8 -*-

from lxml import etree
from requests import get

req = get("http://yuedu.baidu.com/rank/hotsale")
content = req.text
tree = etree.HTML(content)
node = tree.xpath("//div[@class='bd-wrap']//div[@class='booklist-inner clearfix']//div[@class='book']/a")
print len(node)
for x in range(0, len(node)):
    print node[x]

