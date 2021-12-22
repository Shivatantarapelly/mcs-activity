"""
python async is also known as asynchronous function or also known as coroutine in python changes
the behaviour of function call. Async in python is a feature that allows functioning multiple operations
with out wasting time.this being a smart way to handle multiple network task or I/O task where the
actual programmers time is spent waiting for the other task to finish.

Asynchronous functions/ Coroutines uses async keyword OR @asyncio.coroutine.


"""

import asyncio


async def main():
    task = asyncio.create_task(other_function())
    print("apple")
    await asyncio.sleep(1)  # the o/p will be apple,1,banana,2  as after apple we are waiting for 1sec to
    print("banana")  # to execute banana meanwhile because of we used async func it wil print 1 and then
    return_val = await task  # repeats same for banana and 2
    print(return_val)  # storing the return value from other func


async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10  # we can return this value also


asyncio.run(main())
