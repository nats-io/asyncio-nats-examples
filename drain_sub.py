# [begin drain_sub]
import asyncio
from nats.aio.client import Client as NATS

async def example(loop):
    nc = NATS()

    await nc.connect("nats://127.0.0.1:4222", loop=loop)

    async def handler(msg):
        print("[Received] ", msg)
        await nc.publish(msg.reply, b'I can help')

        # Can check whether client is in draining state
        if nc.is_draining:
            print("Connection is draining")

    sid = await nc.subscribe("help", "workers", cb=handler)
    await nc.flush()

    # Gracefully unsubscribe the subscription
    await nc.drain(sid)

# [end drain_sub]

    requests = []
    for i in range(0, 100):
        request = nc.request("help", b'help!', timeout=1)
        requests.append(request)


    # Wait for all the responses
    try:
        responses = []
        responses = await asyncio.gather(*requests)
    except:
        pass

    print("Received {} responses".format(len(responses)))
    await nc.close()



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(example(loop))
    loop.close()
