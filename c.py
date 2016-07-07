# encoding=utf-8

from requests import get
from lxml import etree

for x in range(1, 7):
    h = 't2-p'+str(x)+'.shtml'
    res = get('http://www.jiumei.com/p-list/'+h)
    print res.url
    text = res.text
    # print text
    tree = etree.HTML(text)
    node = tree.xpath("//div[@class='clearfix']//div[@class='gn_m_list_b']/a/@href")
    print node
    print len(node)