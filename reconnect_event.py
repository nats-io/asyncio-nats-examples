import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin reconnect_event]
   nc = NATS()

   async def disconnected_cb():
      print("Got disconnected!")

   async def reconnected_cb():
      # See who we are connected to on reconnect.
      print("Got reconnected to {url}".format(url=nc.connected_url.netloc))

   await nc.connect(
      servers=["nats://127.0.0.1:4222"],
      reconnect_time_wait=10,
      reconnected_cb=reconnected_cb,
      disconnected_cb=disconnected_cb,
      )

   # Do something with the connection.

   # [end reconnect_event]

   while True:
     if nc.is_closed:
       break
     await asyncio.sleep(1)

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
