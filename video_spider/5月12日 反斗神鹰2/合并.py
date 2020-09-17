import os

# 合并视频
filename = '11'
fi = open(f'{filename}.mp4', 'wb')
for i in os.listdir('./'):
    if '.ts' in i:
        print(i)
        with open(i, 'rb') as f:
            fi.write(f.read())
fi.close()
