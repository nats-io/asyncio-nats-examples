import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin ping_5]
   nc = NATS()

   await nc.connect(
      servers=["nats://demo.nats.io:4222"],
      # Set maximum number of PINGs out without getting a PONG back
      # before the connection will be disconnected as a stale connection.
      max_outstanding_pings=5,
      ping_interval=1,
      )

   # Do something with the connection.

   # [end ping_5]

   while True:
     if nc.is_closed:
       break
     await asyncio.sleep(1)

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
