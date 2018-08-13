import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin connect_userpass_url]
   nc = NATS()

   await nc.connect(servers=["nats://myname:password@demo.nats.io:4222"])

   # Do something with the connection.

   # [end connect_userpass_url]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
