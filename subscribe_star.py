import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin subscribe_star]
   nc = NATS()

   await nc.connect(servers=["nats://demo.nats.io:4222"])

   # Use queue to wait for 2 messages to arrive
   queue = asyncio.Queue()
   async def cb(msg):
     await queue.put_nowait(msg)

   await nc.subscribe("time.*.east", cb=cb)

   # Send 2 messages and wait for them to come in
   await nc.publish("time.A.east", b'A')
   await nc.publish("time.B.east", b'B')

   msg_A = await queue.get()
   msg_B = await queue.get()

   print("Msg A:", msg_A)
   print("Msg B:", msg_B)

   # [end subscribe_star]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
