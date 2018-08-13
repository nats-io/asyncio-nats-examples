import asyncio
import json
from nats.aio.client import Client as NATS

async def example():

   # [begin publish_json]
   nc = NATS()

   await nc.connect(servers=["nats://127.0.0.1:4222"])

   await nc.publish("updates", json.dumps({"symbol": "GOOG", "price": 1200 }).encode())

   # [end publish_json]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
