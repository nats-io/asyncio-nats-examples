import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin subscribe_async]
   nc = NATS()

   await nc.connect(servers=["nats://demo.nats.io:4222"])

   future = asyncio.Future()

   async def cb(msg):
     nonlocal future
     future.set_result(msg)

   await nc.subscribe("updates", cb=cb)
   await nc.publish("updates", b'All is Well')
   await nc.flush()

   # Wait for message to come in
   msg = await asyncio.wait_for(future, 1)

   # [end subscribe_async]
   print(msg)

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
