# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LianjiaSpider(CrawlSpider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://hf.lianjia.com/ershoufang/c5111062462639/']

    rules = (
        Rule(LinkExtractor(allow='pg'), follow=True),
        Rule(LinkExtractor(allow=r'ershoufang/\d+'), callback='parse_item', follow=False)
    )

    def parse_item(self, response):
        data = response.xpath('//div[@class="content"]//li/text()').extract()
        print(data)
        # return item
