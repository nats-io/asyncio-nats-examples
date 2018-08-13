import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin subscribe_queue]
   nc = NATS()

   await nc.connect(servers=["nats://127.0.0.1:4222"])

   future = asyncio.Future()

   async def cb(msg):
     nonlocal future
     future.set_result(msg)

   await nc.subscribe("updates", queue="workers", cb=cb)
   await nc.publish("updates", b'All is Well')

   msg = await asyncio.wait_for(future, 1)
   print("Msg", msg)

   # [end subscribe_queue]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
