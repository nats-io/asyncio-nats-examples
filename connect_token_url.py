import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin connect_token_url]
   nc = NATS()

   await nc.connect(servers=["nats://mytoken@demo.nats.io:4222"])

   # Do something with the connection.

   # [end connect_token_url]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
