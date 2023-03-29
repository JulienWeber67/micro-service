import asyncio
import nats
import json

async def reception (message):
    data = json.loads(message.data.decode())
    print (data["ville"])

async def notrefonction():
    nc = await nats.connect("nats://127.0.0.1:4222")
    await nc.subscribe('fr.alsace.67.>', cb = reception)
    await asyncio.sleep(5)
    await nc.close()
    
if __name__=='__main__':    
    asyncio.run(notrefonction())