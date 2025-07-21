import asyncio

async def main():
    async def A():
        await b

    async def B():
        await c

    async def C():
        await a

    async def D():
        await asyncio.sleep(1)
        raise Exception()

    a = asyncio.create_task(A())
    b = asyncio.create_task(B())
    c = asyncio.create_task(C())
    d = asyncio.create_task(D())

    await asyncio.gather(a, d)

asyncio.run(main())