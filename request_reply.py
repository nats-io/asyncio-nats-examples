import asyncio
import json
from nats.aio.client import Client as NATS
from nats.aio.utils import new_inbox

async def example():

   # [begin request_reply]
   nc = NATS()

   async def sub(msg):
     await nc.publish(msg.reply, b'response')

   await nc.connect(servers=["nats://127.0.0.1:4222"])
   await nc.subscribe("time", cb=sub)

   # Send the request
   try:
     msg = await nc.request("time", b'', timeout=1)
     # Use the response
     print("Reply:", msg)
   except asyncio.TimeoutError:
     print("Timed out waiting for response")

   # [end request_reply]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
