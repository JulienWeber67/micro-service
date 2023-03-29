import asyncio
import nats


async def mafonction():
    num = 0
    nc = await nats.connect("nats://127.0.0.1:4222")
    while num != 20 :
        await nc.publish('compteur',str(num).encode())
        await nc.flush()
        num += 2
        await asyncio.sleep(1.0)
    await nc.close()

if __name__ == '__main__':
    asyncio.run(mafonction())
