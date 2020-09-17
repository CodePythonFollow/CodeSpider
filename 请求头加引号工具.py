"""
使用正则表达式将headers转换成python字典格式的工具函数
"""

import re

headers_str = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Cookie: ll="108296"; bid=u7uQV8qAq48; __gads=ID=736cd1a27746d07f:T=1568767437:S=ALNI_MbO0DsElacGED0en44UsxVC59S2ZA; douban-fav-remind=1; viewed="24250054"; gr_user_id=3dc30cfc-7a3e-4c36-a228-045db66b36de; _vwo_uuid_v2=D5AD102F3212719FA6A5C5C43416A7321|d9fed3644bde8c520e9267a1bfb0b37d; dbcl2="193699020:DKJtt7jDaJI"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.19369; douban-profile-remind=1; _ga=GA1.3.244436708.1568767400; ap_v=0,6.0; _gid=GA1.3.1251565782.1570459829; ck=j-MF; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=d296567e-855e-4b98-a476-5f4398a4f5c4; gr_cs1_d296567e-855e-4b98-a476-5f4398a4f5c4=user_id%3A1; __utma=30149280.244436708.1568767400.1570459781.1570463035.6; __utmc=30149280; __utmz=30149280.1570463035.6.6.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_douban=1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_d296567e-855e-4b98-a476-5f4398a4f5c4=true; __utmt=1; __utmb=30149280.4.9.1570463040562; _pk_ref.100001.a7dd=%5B%22%22%2C%22%22%2C1570463042%2C%22https%3A%2F%2Fwww.douban.com%2Fmine%2Forders%2F%22%5D; _pk_ses.100001.a7dd=*; _gat=1; _pk_id.100001.a7dd=2e44bf98a5c3c559.1570110597.3.1570463048.1570459840.
Host: read.douban.com
Pragma: no-cache
Referer: https://read.douban.com/ebook/1076122/
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36
"""

pattern = '^(.*?): (.*)$'  #

#           1     2

for line in headers_str.splitlines():  # 反向引用
    print(re.sub(pattern, '\'\\1\': \'\\2\',', line))
