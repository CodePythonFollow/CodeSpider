# -*- coding: utf-8 -*-
import scrapy
import re
import urllib
from scrapy.linkextractors import LinkExtractor

'''
urllib.parse.unquote 可解决url中文乱码
'''

class ZiciSpider(scrapy.Spider):
    name = 'zici'
    allowed_domains = ['baidu.com']
    start_urls = ['https://hanyu.baidu.com/s?wd=%E4%BD%8F&cf=rcmd&t=img&ptype=zici']

    def parse(self, response):
        # 获取gif 和字名
        gif_pic = response.xpath('//div[@id="header-img"]//img/@data-gif').extract()

        # 保存到管道
        if gif_pic:
            # 获取字名
            url = urllib.parse.unquote(response.url)
            name = re.search('wd=(.*?)&', url).group(1)
            item = {
                'gif_pic': gif_pic[0],
                'name': name
            }
            yield item

        # 循环爬取
        links = LinkExtractor(allow='cf=rcmd&t=img&ptype=zici').extract_links(response)
        for link in links:
            yield scrapy.Request(link.url)

