import asyncio
import aiohttp

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']


@asyncio.coroutine
def call_url(url):
    print('Starting {}'.format(url))
    with aiohttp.ClientSession() as session:
        response = yield from session.get(url)
        data = yield from response.text()
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data


futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
