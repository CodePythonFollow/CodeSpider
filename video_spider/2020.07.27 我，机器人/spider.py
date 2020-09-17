import asyncio
import aiohttp


async def get_ts(url):
    async with aiohttp.ClientSession as session:
        async with await session.get(url) as response:
            print(response.status)


if __name__ == "__main__":
    tasks = []
    with open('1.m3u8') as fi:
        lines = fi.readlines()
    for line in lines:
        if '#' in line:
            pass
        link = 'https://vip.okokbo.com/20171220/lWcOwMO8/800kb/hls/' + line.strip()
        task = asyncio.create_task(get_ts(link))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
