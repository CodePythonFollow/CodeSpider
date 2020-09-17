# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class ZhihuPipeline(object):

    # 打开文件
    def __init__(self):
        self.fi = open('知乎.csv', 'a', encoding='gb18030', newline='')

    # 保存数据
    def process_item(self, item, spider):
        # 转化为列表保存
        writer = csv.writer(self.fi)

        data = [item['name'], item['headline'], item['gender'], item['url']]
        writer.writerow(data)

        # 这里为了在爬取的时候显示我已经保存的的数据
        return item


