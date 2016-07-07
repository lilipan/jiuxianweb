# -*- coding: utf-8 -*-

from requests import get
from lxml import etree
import MySQLdb


class Switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False

f = open("jiuxian.txt", "r")
lines = f.readlines()

for line in lines:
    url = line.strip()
    print url
    res = get(url)
    text = res.content
    tree = etree.HTML(text)
    title = tree.xpath("//div[@class='dIntro clearfix']//h2/text()")
    wine_name = title[0]
    nodes1 = tree.xpath("//div[@class='paraTable']//th[@class='bg']/text()")
    nodes2 = tree.xpath("////div[@class='paraTable']//following-sibling::th[2]/text()")
    # print nodes1
    # print nodes2
    dic = dict(zip(nodes1, nodes2))
    for key in dic.keys():
        # print key
        # print dic[key]
        for case in Switch(key):
            if case('产品类型'.decode('utf-8')):
                pro_type = dic[key]
                break
            if case('香味'.decode('utf-8')):
                smell = dic[key]
                break
            if case('产区'.decode('utf-8')):
                pro_area = dic[key]
                break
            if case('橡木桶陈酿'.decode('utf-8')):
                pro_way = dic[key]
                break
            if case('建议醒酒时间'.decode('utf-8')):
                wake_time = dic[key]
                break
            if case('最佳饮用期'.decode('utf-8')):
                best_time = dic[key]
                break
            if case('色泽'.decode('utf-8')):
                color = dic[key]
                break
            if case('酒庄'.decode('utf-8')):
                wine_chateau = dic[key]
                break
            if case('葡萄品种'.decode('utf-8')):
                grape_var = dic[key]
                break
            if case('口感'.decode('utf-8')):
                taste = dic[key]
                break
            if case('参考年份'.decode('utf-8')):
                year = dic[key]
                break
            if case('等级1'.decode('utf-8')):
                level = dic[key]
                break
            if case('规格'.decode('utf-8')):
                specification = dic[key]
                break
            if case('搭配美食'.decode('utf-8')):
                food = dic[key]
                break
            if case('储藏条件'.decode('utf-8')):
                stor_condition = dic[key]
                break
            if case('净含量'.decode('utf-8')):
                net_content = dic[key]
                break
            if case('酒精度'.decode('utf-8')):
                degree_of_alcohol = dic[key]
                break
            if case('瓶塞'.decode('utf-8')):
                cork = dic[key]
                break
            if case('箱规'.decode('utf-8')):
                carton = dic[key]
                break

    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='admin', db='jiuxian', charset='utf8')
        cur = conn.cursor()
        cur.execute("insert into "
                    "grape_wine(wine_name, pro_type, smell, pro_area, pro_way, wake_time, best_time, color, "
                    "wine_chateau, grape_var, taste, year, level, specification, food, stor_condition, net_content, "
                    "degree_of_alcohol, cork, carton) "
                    "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (wine_name, pro_type, smell, pro_area, pro_way, wake_time, best_time, color, wine_chateau,
                     grape_var, taste, year, level, specification, food, stor_condition, net_content, degree_of_alcohol,
                     cork, carton))
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


# res = get("http://www.jiuxian.com/goods-7490.html")
# tree = etree.HTML(res.content)
# # print type(res.content)
# # print type(res.text)
# nodes = tree.xpath("//div[@class='paraTable']//th|th[@class='bg']")
# for node in nodes:
#     print node.text




