import asyncio
from nats.aio.client import Client as NATS

async def example():
   # [begin reconnect_10x]
   nc = NATS()
   await nc.connect(
      servers=["nats://demo.nats.io:4222"],
      max_reconnect_attempts=10,
      )

   # Do something with the connection

   await nc.close()

   # [end reconnect_10x]

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
