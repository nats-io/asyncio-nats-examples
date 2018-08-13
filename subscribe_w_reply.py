import asyncio
from nats.aio.client import Client as NATS
from nats.aio.utils import new_inbox
from datetime import datetime

async def example():

   # [begin subscribe_w_reply]
   nc = NATS()

   await nc.connect(servers=["nats://127.0.0.1:4222"])

   future = asyncio.Future()

   async def cb(msg):
     nonlocal future
     future.set_result(msg)

   await nc.subscribe("time", cb=cb)

   await nc.publish_request("time", new_inbox(), b'What is the time?')
   await nc.flush()

   # Read the message
   msg = await asyncio.wait_for(future, 1)

   # Send the time
   time_as_bytes = "{}".format(datetime.now()).encode()
   await nc.publish(msg.reply, time_as_bytes)

   # [end subscribe_w_reply]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
