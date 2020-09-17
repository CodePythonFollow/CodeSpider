'''
库
工具包
网络请求包 联网上网站的
数据筛选包
'''

# 网络请求包 需要下载 pip install requests
import requests

# 网页选择器 它能解析html网页代码并且从代码中提取我们想要的数据
'''
pip install bs4
pip install lxml html解析库
'''
from bs4 import BeautifulSoup

'''
爬虫运行流程：
    模拟浏览器向服务器发送http请求(get() post()) 服务器向爬虫返回数据

代码思路：
    1.使用代码去打开书籍详情页，并且返回详情页的所有数据
    2.请求并成功拿到详情页数据之后 去做数据筛选
    3.把筛选好的数据利用文件操作保存到本地
'''

response = requests.get('http://www.biquw.com/book/94/').text
# BeautifulSoup：需要两个参数 参数一 你要筛选哪一个网页 参数二 html解析库
soup = BeautifulSoup(response, 'lxml')

'''
筛选数据的步骤：
    1.提取所有的小说章节名称
    2.提取所有小说章节的a标签中的值，对主域名做字符串拼接
    
    3.在小说内容页中提取内容
        小说内容页是一个单独网页
        所以我们还需要使用requests去请求这个网页
        请求成功之后 进一步的去筛选数据
'''

data_list = soup.find('ul')

for book in data_list.find_all('a'):
    print('{}:{}'.format(book.text, 'http://www.biquw.com/book/94/' + book['href']))
    book_url = 'http://www.biquw.com/book/94/' + book['href']
    data_book = requests.get(book_url).text
    soup = BeautifulSoup(data_book, 'lxml')
    data = soup.find('div', {'id': 'htmlContent'}).text
    # print(data)

    with open(book.text + '.txt', 'w', encoding='utf-8') as f:
        f.write(data)


