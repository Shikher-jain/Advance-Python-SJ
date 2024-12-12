# import time

# def f1():
#     print("f1")
# def f2():
#     print("f2")
# def f3():
#     print("f2")

# f1()
# f2()
# f3()

import asyncio
import time
import requests

async def f1():
    response=requests.get("https://instagram.com/favicon.ico")
    open("instagram1.ico","wb").write(response.content)
    # await asyncio.sleep(1)
    print("f1")
async def f2():
    response=requests.get("https://instagram.com/favicon.ico")
    open("instagram2.ico","wb").write(response.content)
    # await asyncio.sleep(1)
    print("f2")
async def f3():
    response=requests.get("https://instagram.com/favicon.ico")
    open("instagram3.ico","wb").write(response.content)
    # await asyncio.sleep(4)
    print("f3")
    return "abc"
async def main(): 

    # task=asyncio.create_task(f1())
    # # await f1()
    # await f2()
    # await f3()

    L= await asyncio.gather(
        f1(),
        f2(),
        f3(),
    )
    print(L)
asyncio.run(main())