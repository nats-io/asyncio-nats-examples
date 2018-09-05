import asyncio
from nats.aio.client import Client as NATS

async def example():
   # [begin no_echo]
   ncA = NATS()
   ncB = NATS()

   await ncA.connect(no_echo=True)
   await ncB.connect()

   async def handler(msg):
      # Messages sent by `ncA' will not be received.
      print("[Received] ", msg)

   await ncA.subscribe("greetings", cb=handler)
   await ncA.flush()
   await ncA.publish("greetings", b'Hello World!')
   await ncB.publish("greetings", b'Hello World!')

   # Do something with the connection

   await asyncio.sleep(1)
   await ncA.drain()
   await ncB.drain()

   # [end no_echo]

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
loop.close()
