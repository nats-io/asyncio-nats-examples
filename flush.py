import asyncio
from nats.aio.client import Client as NATS

async def example():

   # [begin flush]
   nc = NATS()

   await nc.connect(servers=["nats://demo.nats.io:4222"])

   await nc.publish("updates", b'All is Well')

   # Sends a PING and wait for a PONG from the server, up to the given timeout.
   # This gives guarantee that the server has processed above message.
   await nc.flush(timeout=1)

   # [end flush]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
