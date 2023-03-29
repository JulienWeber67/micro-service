import asyncio
import nats

async def reception (message):
    print (f"message reçu {message.subject}:{message.data.decode()}")

async def notrefonction():
    nc = await nats.connect()
    await nc.subscribe('compteur', cb = reception)
    await asyncio.sleep(15)
    await nc.close()
    
if __name__=='__main__':    
    asyncio.run(notrefonction())
