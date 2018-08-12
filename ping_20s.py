import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin ping_20s]
   nc = NATS()

   await nc.connect(
      servers=["nats://demo.nats.io:4222"],
      # Set Ping Interval to 20 seconds
      ping_interval=20,
      )

   # Do something with the connection.

   # [end ping_20s]

   while True:
     if nc.is_closed:
       break
     await asyncio.sleep(1)

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
