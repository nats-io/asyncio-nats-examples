import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin subscribe_arrow]
   nc = NATS()

   await nc.connect(servers=["nats://127.0.0.1:4222"])

   # Use queue to wait for 4 messages to arrive
   queue = asyncio.Queue()
   async def cb(msg):
     await queue.put(msg)

   await nc.subscribe("time.>", cb=cb)

   # Send 2 messages and wait for them to come in
   await nc.publish("time.A.east", b'A')
   await nc.publish("time.B.east", b'B')
   await nc.publish("time.C.west", b'C')
   await nc.publish("time.D.west", b'D')

   for i in range(0, 4):
     msg = await queue.get()
     print("Msg:", msg)

   await nc.close()

   # [end subscribe_arrow]

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
