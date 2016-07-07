# encoding=utf-8

from requests import get
from lxml import etree

f = open("jiuxian.txt", "w")
for x in range(1, 36):
    payload = {'pageNum': x, 'area': 6}
    res = get('http://list.jiuxian.com/2-0-0-0-0-0-0-0-0-0-0-0.htm', params=payload)
    # print res.url
    text = res.text
    # print text
    tree = etree.HTML(text)
    node = tree.xpath("//div[@class='proListSearch']/ul[@class='clearfix']//div[@class='collect_box']/a/@href")
    print(len(node))
    for y in range(0, len(node)):
        print >> f, node[y]

f.close()

