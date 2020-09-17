import os


# 错误列表
error_num = []
# 合并视频
for num in range(654):
    with open('你的婚礼.mp4', 'ab') as fi:
        if os.path.exists(f'{num}.ts'):
            fo = open(f'{num}.ts', 'rb')
            fi.write(fo.read())
        else:
            # print(f'缺少{num}')
            error_num.append(num)

# 如果合并完成即删除多余文件
if len(error_num) == 0:
    for num in range(654):
        os.remove(f'{num}.ts')
    print('已删除缓存文件')
