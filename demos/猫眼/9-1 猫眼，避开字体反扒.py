'''
爬取猫眼电影名称，评分 以及   票房和介绍

'''

import requests
from lxml import etree
import base64
import csv


class MaoYan():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }
    # 获取详细页网址
    def get_detailurl(self):
        detail_urls = []
        movie_names = []
        movie_scores = []
        url = 'https://maoyan.com/films?showType=1'
        response = requests.get(url, headers=self.headers).text
        html = etree.HTML(response)
        selectors = html.xpath('//dl[@class="movie-list"]//div[@class="movie-item"]')
        # 这样能保证一一对应
        for selector in selectors:
            # 详细页网址
            detail_url = selector.xpath('./a/@href')[0]
            detail_url = 'https://maoyan.com' + detail_url
            detail_urls.append(detail_url)
            # 电影名称
            movie_name = selector.xpath('../div[@class="channel-detail movie-item-title"]/@title')[0]
            movie_names.append(movie_name)
            # 电影评分
            movie_score = selector.xpath('../div[@class="channel-detail channel-detail-orange"]/i/text()')
            if movie_score:
                movie_scores.append(movie_score[0] + movie_score[1])
            else:
                movie_scores.append('暂无评分')        
        return detail_urls, movie_names, movie_scores

    # 得到电影简介
    def get_datas(self, detail_urls):
        movie_introductions = []
        for detail_url in detail_urls:
            res = requests.get(detail_url, headers=self.headers).text
            html = etree.HTML(res)
            movie_introduction = html.xpath('//div[@class="mod-content"]/span/text()')[0]
            movie_introductions.append(movie_introduction)
        return movie_introductions     

    # 得到所有数据
    def go(self):
        detail_urls, movie_names, movie_scores = self.get_detailurl()
        movie_introductions = self.get_datas(detail_urls)
        return movie_names, movie_scores, movie_introductions

    # 保存数据
    def reserve_data(self, movie_names, movie_scores, movie_introductions):
        fi = open('猫眼电影.csv', 'w', encoding='utf-8')
        fi.write('电影名称, 电影评分, 电影简介' + '\n')
        fi.close()
        for movie_name, movie_score, movie_introduction in zip(movie_names, movie_scores, movie_introductions):
            with open('猫眼电影.csv', 'a', encoding='gb18030', newline='') as fi:
                csv_writer = csv.writer(fi)
                csv_writer.writerow([movie_name, movie_score, movie_introduction])
            print(f'{movie_name}保存完成')
        print('已全部保存完成请检查')

    # 实例化时只需调用该方法就能保存数据
    def class_begain(self):
        movie_names, movie_scores, movie_introductions = self.go()
        self.reserve_data(movie_names, movie_scores, movie_introductions)


if __name__ == "__main__":
    maoyan = MaoYan()
    maoyan.class_begain()
    
    
        
