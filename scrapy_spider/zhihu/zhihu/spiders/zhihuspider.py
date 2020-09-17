# -*- coding: utf-8 -*-
import scrapy
import json


class ZhihuspiderSpider(scrapy.Spider):
    name = 'zhihuspider'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v4/members/ponyma/followers?include=data%5B*%5D.answer_count&offset=0&limit=20']

    def parse(self, response):
        datas = json.loads(response.text)
        data = datas.get('data', None)

        item = {}
        for dat in data:
            item['name'] = dat.get('name', None)
            item['headline'] = dat.get('headline', None)
            item['gender'] = dat.get('gender',None)
            item['url'] = dat.get('url')


            # 性别转化
            if item['gender'] == 1:
                item['gender'] = '男'
            elif item['gender'] == 0:
                item['gender'] = '女'
            else:
                item['gender'] = None

            yield item

        # 下一页网址，循环到结束
        if datas['paging']:
            if datas['paging']['next']:
                nextpage = datas['paging']['next']
                nextpage = nextpage.replace('members', 'api/v4/members')
                # print(nextpage)
                yield scrapy.Request(nextpage)

        # 每一个粉丝的url
        for dat in data:
            url_token = dat.get('url_token')
            fens_url = f'https://www.zhihu.com/api/v4/members/{url_token}/followers?include=data%5B*%5D.answer_count&offset=0&limit=20'
            # print(fens_url)
            return scrapy.Request(fens_url)

