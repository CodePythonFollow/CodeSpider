import requests

ls =[]
for i in range(928):
    if len(str(i)) == 1:
        num = '00' + str(i)
        ls.append(num)
    elif len(str(i)) == 2:
        num = '0' + str(i)
        ls.append(num)
    else:
        ls.append(str(i))


urls = [f'https://www7.laqddcc.com/hls/2019/08/30/cZpj5rtM/out{num}.ts' for num in ls]

for url in urls:
    response = requests.get(url, verify=False)
    with open('阴曹使者.mp4', 'ab') as fi:
        fi.write(response.content)