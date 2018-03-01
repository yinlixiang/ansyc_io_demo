import asyncio
import aiohttp

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']


async def call_url(url):
    print('Starting {}'.format(url))
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.text()
        print('{}: {} bytes: {}'.format(url, len(data), data))
        return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
