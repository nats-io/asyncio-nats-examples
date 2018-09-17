# [begin connect_tls_url]
import asyncio
import ssl
import certifi
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrTimeout

async def run(loop):
    nc = NATS()

    # Using certificates bundle provided via 'certifi' package.
    ssl_ctx = ssl.create_default_context()
    ssl_ctx.load_verify_locations(certifi.where())
    await nc.connect(servers=["tls://demo.nats.io:4443"], loop=loop, tls=ssl_ctx)

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))

    # Simple publisher and async subscriber via coroutine.
    sid = await nc.subscribe("foo", cb=message_handler)
    await nc.flush()

    # Stop receiving after 2 messages.
    await nc.auto_unsubscribe(sid, 2)
    await nc.publish("foo", b'Hello')
    await nc.publish("foo", b'World')
    await nc.publish("foo", b'!!!!!')
    await asyncio.sleep(1, loop=loop)
    await nc.close()
# [end connect_tls_url]

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.close()
