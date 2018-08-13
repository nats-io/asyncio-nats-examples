import asyncio
import ssl
from nats.aio.client import Client as NATS

async def example():

   # [begin connect_tls]
   nc = NATS()

   ssl_ctx = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
   ssl_ctx.load_verify_locations('ca.pem')
   ssl_ctx.load_cert_chain(certfile='client-cert.pem',
                           keyfile='client-key.pem')
   await nc.connect(io_loop=loop, tls=ssl_ctx)

   await nc.connect(servers=["nats://127.0.0.1:4222"], tls=ssl_ctx)

   # Do something with the connection.

   # [end connect_tls]

   await nc.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
