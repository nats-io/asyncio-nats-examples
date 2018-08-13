import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin connect_name]
   nc = NATS()

   await nc.connect(servers=["nats://demo.nats.io:4222"], name="my-connection")

   # Do something with the connection.

   # [end connect_name]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
