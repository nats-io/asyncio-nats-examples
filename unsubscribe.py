import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin unsubscribe]
   nc = NATS()

   await nc.connect(servers=["nats://demo.nats.io:4222"])

   future = asyncio.Future()

   async def cb(msg):
     nonlocal future
     future.set_result(msg)

   sid = await nc.subscribe("updates", cb=cb)
   await nc.publish("updates", b'All is Well')

   # Remove interest in subject
   await nc.unsubscribe(sid)

   # Won't be received...
   await nc.publish("updates", b'...')

   # [end unsubscribe]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
