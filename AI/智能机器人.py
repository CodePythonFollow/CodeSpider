#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json, time, random

feature_text = '''
大家好！我是你的聊天机器人小可爱。

我有问必答，有人会问我“今天淮南天气怎么样？”，也有人问我“你喜欢我吗？”
快来问我问题呀，欢迎来撩！
>'''

user1 = input(feature_text)
time.sleep(1)
userid = str(random.randint(1, 1000000000000000000000))
apikey = 'd81c0b99c260440980a140440be200ec'
#超过1w有风险，19-01-19
tulingdata1 = json.dumps({    "perception": {
        "inputText": {
            "text": user1
        },

    },
    "userInfo": {
        "apiKey": apikey,
        "userId": userid
    }
})
robot1 = requests.post('http://openapi.tuling123.com/openapi/api/v2', tulingdata1)
jsrobot1 = json.loads(robot1.text)['results'][0]['values']['text']
print(jsrobot1)
time.sleep(2)
user2 = input('''
再来问我点啥吧！我把我知道的都告诉你，嘻嘻！
>''')
tulingdata1 = json.dumps({
    "perception": {
        "inputText": {
            "text": user2
        },

    },
    "userInfo": {
        "apiKey": apikey,
        "userId": userid
    }
})
robot1 = requests.post('http://openapi.tuling123.com/openapi/api/v2', tulingdata1)
jsrobot1 = json.loads(robot1.text)['results'][0]['values']['text']
time.sleep(1)
print(jsrobot1)
user3 = input('''
我有点饿了，再和你聊完最后一句，我就要下线啦！你还有什么要问我的？
>''')
tulingdata1 = json.dumps({
    "perception": {
        "inputText": {
            "text": user3
        },

    },
    "userInfo": {
        "apiKey": apikey,
        "userId": userid
    }
})
robot1 = requests.post('http://openapi.tuling123.com/openapi/api/v2', tulingdata1)
jsrobot1 = json.loads(robot1.text)['results'][0]['values']['text']
time.sleep(1)
print(jsrobot1)
time.sleep(1)
print('\n我走啦，下次见！')