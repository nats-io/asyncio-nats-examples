import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin unsubscribe_auto]
   nc = NATS()

   await nc.connect(servers=["nats://demo.nats.io:4222"])

   async def cb(msg):
     print(msg)

   sid = await nc.subscribe("updates", cb=cb)
   await nc.auto_unsubscribe(sid, 1)
   await nc.publish("updates", b'All is Well')

   # Won't be received...
   await nc.publish("updates", b'...')

   # [end unsubscribe_auto]

   await asyncio.sleep(1)

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
