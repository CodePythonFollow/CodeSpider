# -*- coding: utf-8 -*-
import scrapy
import json


class ShujiSpider(scrapy.Spider):
    name = 'shuji'
    allowed_domains = ['ximalaya.com']
    start_urls = [f'https://www.ximalaya.com/revision/category/queryCategoryPageAlbums?category=jiaoyu&subcategory=xinmeiti&meta=6_2592&sort=0&page={num}&perPage=30' for num in range(1, 11)]

    def parse(self, response):
        # 获得title和albumId和anchorName和link
        json_data = json.loads(response.text)
        if json_data.get("data", None):
            if json_data['data'].get('albums', None):
                for book_data in json_data['data']['albums']:
                    albumId = book_data['albumId']
                    title = book_data['title']
                    anchorName = book_data['anchorName']
                    link = book_data['link']
                    item = {
                        'albumId': albumId,
                        'title': title,
                        'anchorName': anchorName,
                    } 
                    # 构造详细页网址
                    detail_url = response.urljoin(link)
                    print(detail_url)
                    yield scrapy.Request(detail_url, callback=self.deal_detail, meta=item)                    

        
            
    # 提取详细页数据
    def deal_detail(self, response):
        
        # 因为这个小漏洞所以try一下
        introduction = response.xpath('//div/article/p/text()').extract()
        '''
            get() 只提取一个
            extract() 可以提取所有的
            有一个小漏洞 p标签下的span标签文本未提取出来，可能会影响读取
        '''
        # print(introduction)
        item = {
            'introduction': introduction,
            'albumId': response.meta['albumId'],
            'title': response.meta['title'],
            'anchorName': response.meta['anchorName']
        }
        yield item