#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree
import re
from fontTools.ttLib import TTFont

class Qidian():

    def __init__(self):
        # 请求头属性
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    # 获得需要解密的html文件以及字体映射链接
    def get_html(self, detail_url):
        '''
        :param url:
        :return:
        '''
        html = requests.get(detail_url, headers=self.headers).text
        font_link = re.search("format\('eot'\); src: url\('(.*?)'\) format\('woff'\)", html).group(1)

        return html, font_link

    # 获得字体下载映射关系
    def get_fontmap(self, font_link):
        '''返回映射关系'''
        response = requests.get(font_link)
        with open('字体文件.woff', 'wb') as fi:
            fi.write(response.content)
        fi = TTFont('字体文件.woff')
        fi.saveXML('font.xml')
        font_map = fi['cmap'].getBestCmap()

        # 把对应关系换成我们能识别的数字
        d = {
            'period': '.', 'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
        }
        for key in font_map:
            font_map[key] = d[font_map[key]]

        return font_map

    # 替换源网页，并返回替换后的html文件
    def get_new_html(self, font_map, html):
        '''返回解密的html文件'''
        for key in font_map:
            html = html.replace('&#' + str(key) + ';', font_map[key])

        return html

    # 得到详细页网址
    def get_detailurl(self, page):
        '''
        :param page:
        :return link_list:
        '''
        url = f'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page={page}'
        response = requests.get(url, headers=self.headers).text
        html = etree.HTML(response)
        selectors = html.xpath('//ul[@class="all-img-list cf"]//li')
        for selector in selectors:
            # 小说详细页网址
            detail_url = selector.xpath('./div[@class="book-mid-info"]/h4/a/@href')[0]

            yield 'http:' + detail_url


if __name__ == "__main__":
    qidian = Qidian()
    # 第一页
    for detail_url in qidian.get_detailurl(1):
        html, font_link = qidian.get_html(detail_url)
        font_map = qidian.get_fontmap(font_link)
        # time.sleep(3)
        # print(font_map)
        new_html = qidian.get_new_html(font_map, html)
        print(new_html)


