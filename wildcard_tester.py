import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin wildcard_tester]
   nc = NATS()

   await nc.connect(servers=["nats://127.0.0.1:4222"])

   await nc.publish("time.us.east", b'...')
   await nc.publish("time.us.east.atlanta", b'...')

   await nc.publish("time.eu.east", b'...')
   await nc.publish("time.eu.east.warsaw", b'...')

   await nc.close()

   # [end wildcard_tester]

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
