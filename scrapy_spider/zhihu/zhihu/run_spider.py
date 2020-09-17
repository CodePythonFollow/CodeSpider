#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: run_spider.py
@time: 2019/9/24 12:58
'''
from scrapy import cmdline
cmdline.execute('scrapy crawl zhihuspider'.split())