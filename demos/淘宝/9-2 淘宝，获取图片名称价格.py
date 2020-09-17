import requests
import urllib.request
import re
import os

class Taobao():

    # noinspection PyInterpreter
    def __init__(self):
        # 设置请求头
        self.headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'miid=1450411095727420042; t=da3fe90eb4c62e0c694e0fe2ff87548a; cna=RybuFUFHrXwCATyvXUWK0RaB; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _m_h5_tk=836b73e0026eb611c1eb46622f3294cd_1567086744674; _m_h5_tk_enc=a9c4bf490b53d6d18553a40c99f054a6; uc3=nk2=qh7Dr2ngNlJ0&vt3=F8dBy3MGaTIcA66Klmg%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=UNN0mTwTHBdNRQ%3D%3D; lgc=%5Cu795E%5Cu79D8%5Cu5962%5Cu534Eq; uc4=id4=0%40UgQ8cvT6zPQcbkwi0OUeJqwmHon1&nk4=0%40qCSYOKQ119kQt8QSysPwOI1SEco%3D; tracknick=%5Cu795E%5Cu79D8%5Cu5962%5Cu534Eq; _cc_=UIHiLt3xSw%3D%3D; tg=0; enc=XSi9PmISyXG%2B94I13Z4l0yKT2ixxnPmOzWDKmtfUASok1GD09%2FQz2blqLYbTvMbAN%2FzgdrrVyNfzks97gn2K9Q%3D%3D; mt=ci=10_1; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; UM_distinctid=16cf01ac71444a-04db703053f90a-e343166-144000-16cf01ac71571b; v=0; cookie2=513750aafa67c5f240200e0e2c891b06; _tb_token_=f4fb33bb5306b; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; swfstore=291295; x5sec=7b227365617263686170703b32223a223035313964313264313833363731316131613435336461633638366265366563434e6e48744f7346454c2b476a6565696d642f787851456144444d7a4f5441314d446b344f5441374f413d3d227d; JSESSIONID=41541EF8C9903C2BC69794D4E16887A4; l=cBSWq7slqF7rnZCBBOfZlurza77O2QRb8sPzaNbMiICP9Xf9tOzcWZEQsyYpCnGVL6zvR3SgKvQUBbYL1PatC1fm22YCgsDd.; isg=BP39jexNfHGNjNiXF7stTc1pDFn3mjHs7TpuXb9AhtTc9h8oh-q5vuXsoGoV9kmk; uc1=cookie14=UoTaH0O3h%2FbEJg%3D%3D',
            'referer': f'https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        }

    # 获取图片
    def get_picture(self):
        '''返回图片的url'''
        url = f'https://s.taobao.com/search?data-key=s&data-value=88&ajax=true&_ksTS=1567430930057_1108&callback=jsonp1109&q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s=44'
        response = requests.get(url, headers=self.headers).text

        # 最好不要删，验证cookie是否失效
        # 因为cookie是js加密的
        print(response)
        names = re.findall('"title":"(.*?)"', response, re.S)
        picture_urls = re.findall('"pic_url":"(.*?)"', response, re.S)

        # 保存数据，由于容易失效写在一个函数
        if not os.path.exists('淘宝图片'):
            os.mkdir('淘宝图片')
        for name, picture_url in zip(names, picture_urls):
            url = 'http:' + picture_url
            # 注意点name 里面有'/'会影响后面的路径
            name = name.split('\\')[0]
            name = name.replace('/', ',')

            urllib.request.urlretrieve(url, '淘宝图片' + '/' + name + '.jpg')



if __name__ == "__main__":
    shouji = Taobao()
    shouji.get_picture()

