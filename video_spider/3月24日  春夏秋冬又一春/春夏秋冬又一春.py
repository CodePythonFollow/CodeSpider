import requests
import threading
import os

# https://leshi.iqiyi-kuyunzy.com/20190309/4698_f6394cb6/800k/hls/90b26b0e52c000000.ts
# 90b26b0e52c001574.ts
headers = {
    # 'accept': '*/*',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'if-modified-since': 'Sat, 09 Mar 2019 09:50:34 GMT',
    # 'if-none-match': "5c838c6a-8aa8c",
    # 'origin': 'https://gimy.tv',
    'referer': 'https://gimy.tv/vod-play-id-99021-src-1-num-1.html',
    # 'sec-fetch-dest': 'empty',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36'
}


# 多线程
sem = threading.Semaphore(4)


def run(num, url):
    if os.path.exists(f'{num}.ts'):
        pass
    else:
        # print(num)
        # print()
        response = requests.get(url, headers=headers, timeout=7)
        fi = open(f'{num}.ts', 'wb')
        fi.write(response.content)


if __name__ == "__main__":
    # 构建网址
    urls = []
    for i in range(0, 1575):
        zero_num = 4 - len(str(i))
        ts = '0' * zero_num + str(i)
        url = f'https://leshi.iqiyi-kuyunzy.com/20190309/4698_f6394cb6/800k/hls/90b26b0e52c00{ts}.ts'
        urls.append(url)
    # 多线程下载
    for num, url in enumerate(urls):
        # print(num, url)
        t = threading.Thread(target=run, args=(num, url))
        with sem:
            # print(t.name)
            t.start()
