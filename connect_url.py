import asyncio
from nats.aio.client import Client as NATS

async def example():
   # [begin connect_url]
   nc = NATS()
   await nc.connect(servers=["nats://demo.nats.io:4222"])

   # Do something with the connection

   await nc.close()

   # [end connect_url]

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
