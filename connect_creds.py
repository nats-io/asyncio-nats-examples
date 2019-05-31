import asyncio
from nats.aio.client import Client as NATS

async def example():
   # [begin connect_creds]
   nc = NATS()

   async def error_cb(e):
       print("Error:", e)

   await nc.connect("nats://localhost:4222",
                    user_credentials="path_to_creds_file",
                    error_cb=error_cb,
                    )

   # Do something with the connection

   await nc.close()

   # [end connect_creds]

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
