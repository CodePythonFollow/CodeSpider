#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests
'''
   # 因为数据都解析完成，所以每行数据理论上不会有逗号，否则保存应该采用 行的方式写入
'''

fi = open('搜狐数据.csv', 'a')
fi.write('品牌名,公司名称,型号,日期,销量/个' + '\n')

all_url = 'http://db.auto.sohu.com/cxdata/xml/basic/modelList.xml'

response = requests.get(all_url).text
# print(response)
brandnames = re.findall('<model brandName="(.*?)" corpName=', response)
# print(len(brandname))
corpNames = re.findall('corpName="(.*?)" name=', response)
# print(len(corpName))
names = re.findall('name="(.*?)" id=', response)
# print(len(name))
ids = re.findall('id="(.*?)" brandId=', response)
# print(len(ids))

# 用来得到单个型号的车辆所有数据
list = []
for brandname, corpName, name, id in zip(brandnames, corpNames, names, ids):
    # 构造网址得到销量数据
    url = f'http://db.auto.sohu.com/cxdata/xml/sales/model/model{id}sales.xml'
    res = requests.get(url).text
    datas = re.findall('date="(.*?)"', res)
    sale_nums = re.findall('salesNum="(.*?)"', res)
    for data, sale_num in zip(datas, sale_nums):
        # print(brandname, corpName, name, data, sale_num)
        fi.write(f'{brandname},{corpName},{name},{data},{sale_num}' + '\n')
    print(brandname + '的' + name + '车型' + '月已保存完毕')
print('保存完毕请检查')

fi.close()


