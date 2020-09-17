import os


c = 0
for i in os.listdir('./'):
    if 'ts' in i:
        c += 1

# 合并视频
filename = '我，机器人'
fi = open(f'{filename}.mp4', 'ab')


for i in range(c):
    with open(f'{i}.ts', 'rb',) as f:
        fi.write(f.read())
    os.remove(f'{i}.ts')