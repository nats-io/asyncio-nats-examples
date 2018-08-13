import asyncio
import json
from nats.aio.client import Client as NATS
from nats.aio.utils import new_inbox

async def example():

   # [begin publish_with_reply]
   nc = NATS()

   future = asyncio.Future()

   async def sub(msg):
     nonlocal future
     future.set_result(msg)

   await nc.connect(servers=["nats://demo.nats.io:4222"])
   await nc.subscribe("time", cb=sub)

   unique_reply_to = new_inbox()
   await nc.publish_request("time", unique_reply_to, b'')

   # Use the response
   msg = await asyncio.wait_for(future, 1)
   print("Reply:", msg)

   # [end publish_with_reply]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
