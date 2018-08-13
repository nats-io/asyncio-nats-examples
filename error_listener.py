import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin error_listener]
   nc = NATS()

   async def error_cb(e):
      print("Error: ", e)

   await nc.connect(
      servers=["nats://demo.nats.io:4222"],
      reconnect_time_wait=10,
      error_cb=error_cb,
      )

   # Do something with the connection.

   # [end error_listener]

   while True:
     if nc.is_closed:
       break
     await asyncio.sleep(1)

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
