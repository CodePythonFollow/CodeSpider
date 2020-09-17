# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request

class BaiduzicispiderPipeline(object):

    # 保存数据
    def process_item(self, item, spider):
        filename = item['name']
        urllib.request.urlretrieve(item['gif_pic'], f'E:\spider\每日爬虫\百度汉字\文字\{filename}.gif')
        return item










