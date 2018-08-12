import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin connect_pedantic]
   nc = NATS()

   await nc.connect(servers=["nats://127.0.0.1:4222"], pedantic=True)

   # Do something with the connection.

   # [end connect_pedantic]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
