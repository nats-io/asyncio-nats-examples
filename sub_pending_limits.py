import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin slow_pending_limits]
   nc = NATS()

   await nc.connect(servers=["nats://demo.nats.io:4222"])

   future = asyncio.Future()

   async def cb(msg):
     nonlocal future
     future.set_result(msg)

   # Set limits of 1000 messages or 5MB
   await nc.subscribe("updates", cb=cb, pending_bytes_limit=5*1024*1024, pending_msgs_limit=1000)

   # [end slow_pending_limits]

   await nc.publish("updates", b'All is Well')
   await nc.flush()

   # Wait for message to come in
   msg = await asyncio.wait_for(future, 1)


   print(msg)

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
