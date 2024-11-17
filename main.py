import base64
import httpx
import random
import time
import json
import uuid
import asyncio
from fake_useragent import UserAgent
import requests
from defs import *
import uuid
import re
from html import unescape


def gets(s, start, end):
            try:
                start_index = s.index(start) + len(start)
                end_index = s.index(end, start_index)
                return s[start_index:end_index]
            except ValueError:
                return None



async def create_payment_method(fullz, session):
    try:

        cc, mes, ano, cvv = fullz.split("|")

    
        user = "cristniki" + str(random.randint(9999, 574545))
        mail = "cristniki" + str(random.randint(9999, 574545))+"@gmail.com"

















    except Exception as e:
        print(e)
        return str(e)


async def multi_checking(x):
    start = time.time()
    getproxy = random.choice(
        open("proxy.txt", "r", encoding="utf-8").read().splitlines())
    proxy_ip = getproxy.split(":")[0]
    proxy_port = getproxy.split(":")[1]
    proxy_user = getproxy.split(":")[2]
    proxy_password = getproxy.split(":")[3]
    proxies = {
        "https://": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
        "http://": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
    }
    session = httpx.AsyncClient(timeout=40, proxies=proxies)
    # session = httpx.AsyncClient(timeout=40,)
    result = await create_payment_method(x, session)
    response = await charge_resp(result)
    resp = f"{x} - {response} - Taken {round(time.time() - start, 2)}s"
    print(resp)
    if "Charged 1$ 🔥" in response or "CCN Live ❎" in response or "CVV LIVE ❎" in response:
        # charge test
        with open("charge.txt", "a", encoding="utf-8") as file:
            file.write(resp + "\n")
    await session.aclose()
    await asyncio.sleep(0.5)


async def main():
    ccs = open("ccs.txt", "r", encoding="utf-8").read().splitlines()

    # for x in ccs:
    #    await multi_checking(x)
    #    exit()

    works = [multi_checking(i) for i in ccs]
    worker_num = 15
    while works:
        a = works[:worker_num]
        a = await asyncio.gather(*a)
        works = works[worker_num:]

if __name__ == "__main__":
    asyncio.run(main())
