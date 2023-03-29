import asyncio
import nats
import json

async def mafonction():
    while True :
        nc = await nats.connect("nats://127.0.0.1:4222")
        await nc.publish("fr.alsace.67.Strasbourg",json.dumps({"pays": "fr","region": "alsace","departement": 67,"ville":"Strasbourg"}).encode())
        await nc.publish("fr.alsace.68.Colmar",json.dumps({"pays": "fr","region": "alsace","departement": 67,"ville":"Colmar"}).encode())
        await nc.publish("fr.alsace.67.Haguenau",json.dumps({"pays": "fr","region": "alsace","departement": 67,"ville":"Haguenau"}).encode())
        await nc.publish("eau.viande.69.Strasbourg",json.dumps({"pays": "fr","region": "alsace","departement": 67,"ville":"Strasbourg2"}).encode())
        await nc.flush()
        await asyncio.sleep(1.0)

if __name__ == '__main__':
    asyncio.run(mafonction())