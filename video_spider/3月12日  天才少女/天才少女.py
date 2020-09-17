import requests
import threading
import os

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'http://api.oopw.top',
    'pragma': 'no-cache',
    'referer': 'http://api.oopw.top/player/p2p-dplayer/?live=0&autoplay=1&url=https%3A%2F%2Fyouku.com-t-youku.com%2F20190316%2F8844_d7327392%2Findex.m3u8&logo_off=0&logo_style=bGVmdDowcHg7IHRvcDo1MHB4O21heC13aWR0aDoxMDBweDttYXgtaGVpZ2h0OjEwMHB4&ver=x&p2pinfo=1&posterr=1&seektime=1&danmaku=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}


# 多线程
sem = threading.Semaphore(4)


def run(num, url):
    if os.path.exists(f'{num}.ts'):
        pass
    else:
        print(num)
        print()
        # response = requests.get(url, headers=headers, timeout=5)
        # fi = open(f'{num}.ts', 'wb')
        # fi.write(response.content)


if __name__ == "__main__":
    # 构建网址
    urls = []
    for i in range(0, 1515):
        zero_num = 4 - len(str(i))
        ts = '0' * zero_num + str(i)
        url = f'https://youku.com-t-youku.com/20190316/8844_d7327392/1000k/hls/c362a9ae29400{ts}.ts'
        urls.append(url)
    # 多线程下载
    for num, url in enumerate(urls):
        # print(num, url)
        t = threading.Thread(target=run, args=(num, url))
        with sem:
            # print(t.name)
            t.start()
