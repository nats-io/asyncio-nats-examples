import asyncio
from nats.aio.client import Client as NATS

async def example():
   # [begin connect_nkey]
   nc = NATS()

   async def error_cb(e):
       print("Error:", e)

   await nc.connect("nats://localhost:4222",
                    nkeys_seed="./path/to/nkeys/user.nk",
                    error_cb=error_cb,
                    )

   # Do something with the connection

   await nc.close()

   # [end connect_nkey]

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
