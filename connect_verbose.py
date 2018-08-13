import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin connect_verbose]
   nc = NATS()

   await nc.connect(servers=["nats://127.0.0.1:4222"], verbose=True)

   # Do something with the connection.

   # [end connect_verbose]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
