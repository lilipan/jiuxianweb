# encoding=utf-8

import requests
import re

r1 = re.compile('^<!-- 商品列表begin*商品列表end -->$')

r = re.compile('http://www.jiuxian.com/goods-\d+\.html')

res = requests.get('http://list.jiuxian.com/2-0-0-0-0-0-0-0-0-0-0-0.htm?pageNum=1&&area=6')

print res.text

result1 = r1.search(res.text)

# result = r.findall(res.text)

print(result1)


