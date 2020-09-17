# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class XimalayaspiderPipeline(object):
    # 打开文件
    def __init__(self):
        self.file = open('喜马拉雅数据.text', 'a', encoding='utf-8')
    # 保存文件
    def process_item(self, item, spider):
        self.file.write(json.dumps(item, ensure_ascii=False) + '\n')
        return item
    # 关闭文件 
    def close_spider(self, spider):
        self.file.close()