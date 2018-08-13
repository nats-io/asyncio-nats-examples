import asyncio
from nats.aio.client import Client as NATS

async def example():
   # [begin reconnect_no_random]
   nc = NATS()
   await nc.connect(
      servers=[
         "nats://demo.nats.io:1222",
         "nats://demo.nats.io:1223",
         "nats://demo.nats.io:1224"
         ],
      dont_randomize=True,
      )

   # Do something with the connection

   await nc.close()

   # [end reconnect_no_random]

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
