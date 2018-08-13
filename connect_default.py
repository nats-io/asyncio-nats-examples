import asyncio
from nats.aio.client import Client as NATS

async def example():
   # [begin connect_default]
   nc = NATS()
   await nc.connect()

   # Do something with the connection

   await nc.close()

   # [end connect_default]

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
