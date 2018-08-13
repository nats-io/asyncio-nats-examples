import asyncio
from nats.aio.client import Client as NATS

async def example():
   # [begin reconnect_10s]
   nc = NATS()
   await nc.connect(
      servers=["nats://demo.nats.io:4222"],
      reconnect_time_wait=10,
      )

   # Do something with the connection

   await nc.close()

   # [end reconnect_10s]

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
