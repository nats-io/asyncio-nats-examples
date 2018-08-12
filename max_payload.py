import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin max_payload]
   nc = NATS()

   await nc.connect(servers=["nats://demo.nats.io:4222"])

   print("Maximum payload is %d bytes" % nc.max_payload)

   # Do something with the max payload.

   # [end max_payload]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
