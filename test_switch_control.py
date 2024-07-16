import os
import sys
dynamic_path = os.path.abspath(__file__ + "/../../")
# print(dynamic_path)
sys.path.append(dynamic_path)
import asyncio
from kasa import Discover
from kasa import SmartPlug
from pprint import pformat as pf
import time

async def main():
    # device = await Discover.discover()
    # print("looked for device")
    # for addr, dev in device.items():
    #     await dev.update()
    #     print(f'{addr}: {dev}')
    # print("looking for specific plug")

    plug = SmartPlug("10.42.0.99")
    await plug.update()
    print("Hardware: %s" % pf(plug.hw_info))
    print("Full sysinfo: %s" % pf(plug.sys_info))
    print("Current state: %s" % plug.is_on)
    start_time = time.time()
    iterations = 10
    sleepTime = 0.200 #s
    for i in range(iterations):
        await plug.turn_on()
        time.sleep(sleepTime/2)
        # input('Press Enter to continue...')
        await plug.turn_off()
        time.sleep(sleepTime/2)
        # input('Press Enter to continue...')
    time_elapsed = time.time() - start_time
    print('Finished in {} seconds'.format(time.time() - start_time))
    print('Frequency = ' + str(iterations/time_elapsed) + "Hz")

if __name__ == '__main__':
    asyncio.run(main())