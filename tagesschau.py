#!/usr/bin/env python3
import requests
import socket
from time import sleep
import os
import re
import sys

if len(sys.argv) > 1: 
    player = sys.argv[1]
else:
    player = "castnow"
url = "https://www.tagesschau.de/multimedia/"
legit_types = [0000, 3400, 2000]
pattern = re.compile(
        r"https://download\.media\.tagesschau\.de/video/\d\d\d\d/\d\d\d\d/TV-\d\d\d\d\d\d\d\d-\d\d\d\d-\d\d00\.webxl\.h264\.mp4"
        )

def wait_till_online():
    try:
        host = socket.gethostbyname("tagesschau.de")
    except:
        sleep(1)
        print("offline")
        wait_till_online()

def get_all_mp4():
    page = requests.get(url).text
    matches = pattern.finditer(page)
    return matches


def get_valid_urls(mp4s):
    urls = []
    for  mp4 in mp4s:
        url  = mp4.group(0)
        type = int(url[-19:-15])
        for legit in legit_types:
            if type == legit:
                print(url)
                urls.append(url)
    return urls

def get_latest(urls):
    return  urls[-1]

wait_till_online()
mp4s = get_all_mp4()
urls = get_valid_urls(mp4s)
url = get_latest(urls)
cmd = f"{player} {url}"
os.system(cmd)
