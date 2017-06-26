import asyncio

loop = asyncio.get_event_loop()

async def hello():
    print('hello')
    await asyncio.sleep(3)
    print('World!')

if __name__ == '__main__':
    for i in range(0,11):
        loop.run_until_complete(hello())
