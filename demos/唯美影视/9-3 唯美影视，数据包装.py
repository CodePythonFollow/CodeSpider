#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import csv
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

# 得到所有详细页网址,输出为生成器
def get_detailurl(page):
    '''获取详细页网址'''
    url = f'http://www.wmpic.me/Movie/typelist/p/{page}.html'
    # 获得响应
    response = requests.get(url, headers=headers).text
    # 转化html
    html = etree.HTML(response)
    # 得到selectors
    selectors = html.xpath('//ul//li')
    # 获得详细页网址和评分
    for selector in selectors:
        # 获取详细页网址
        movie_url = selector.xpath('./a[1]/@href')[0]
        # 获得评分
        movie_score = selector.xpath('./a[1]/span/text()')[0]
        # 构建数据
        item = {
            'movie_urls': movie_url,
            'movie_score': movie_score
        }
        yield item

# 得到单个电影网址和评分数据
def get_data(item):
    '''得到一个列表包含所有数据'''
    # 构件链接
    movie_url = 'http://www.wmpic.me' + item['movie_url']
    # 获取响应
    response = requests.get(movie_url, headers=headers).text
    # 得到html
    html = etree.HTML(response)
    # 电影名称
    movie_name = html.xpath('//dl/dt/text()')
    # 电影类型
    movie_type = html.xpath('//dl/dd[1]/a/text()')
    # 地区
    movie_id = html.xpath('//dl/dd[2]/a')
    # 时长
    movie_time = html.xpath('//dl/dd[3]/text()')
    # 上映时间
    release_time = html.xpath('//dl/dd[4]/text()')
    # 主演
    movie_stars = html.xpath('//dl/dd[5]/text()')
    # 剧情介绍
    movie_introduction = html.xpath('/html/body/div[2]/div[1]/div[3]/div[2]/text()')
    # 得到数据
    data = [
        movie_name, item['movie_score'], movie_type, movie_id, movie_time, release_time, movie_stars, movie_introduction
   ]

    return data

# 保存单个数据
def reserve_data(data):
    fi = open('唯美影视.csv', 'w')
    fi.write('电影名称,评分,类型,区域,时长,上映时间,主演,简介' + '\n')
    fi.close()
    with open('唯美影视.csv', 'a', encoding='utf-8', newline='') as fi:
        writer = csv.writer(fi)
        writer.writerow(data)

if __name__ == "__main__":
    '''这里的组合就看大家了，加一个条件遍历每一页,爬取全站电影'''