import asyncio
from nats.aio.client import Client as NATS

async def example():
   # [begin connect_options]
   nc = NATS()
   await nc.connect(connect_timeout=2)

   # Do something with the connection

   await nc.close()

   # [end connect_options]

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
