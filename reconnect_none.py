import asyncio
from nats.aio.client import Client as NATS

async def example():
   # [begin reconnect_none]
   nc = NATS()
   await nc.connect(
      servers=[
         "nats://demo.nats.io:1222",
         "nats://demo.nats.io:1223",
         "nats://demo.nats.io:1224"
         ],
      allow_reconnect=False,
      )

   # Do something with the connection

   await nc.close()

   # [end reconnect_none]

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
