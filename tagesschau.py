#!/usr/bin/env python3
import requests
import socket
from time import sleep
import os
import re
player = "mpv"
def wait_till_online():
    try:
        host = socket.gethostbyname("google.com")
    except:
        sleep(1)
        wait_till_online()

wait_till_online()

url = "https://www.tagesschau.de/"
page = requests.get(url).text
pattern = re.compile(
        r"https://download\.media\.tagesschau\.de/video/\d\d\d\d/\d\d\d\d/TV-\d\d\d\d\d\d\d\d-\d\d\d\d-\d\d00\.webxl\.h264\.mp4"
        )
matches = pattern.finditer(page)
urls = []
legit_types = [0000, 3400]
for match in matches:
    url  = match.group(0)
    type = int(url[-19:-15])
    for legit in legit_types:
        if type == legit:
            urls.append(url)

url = urls[-1]
cmd = f"{player} {url}"
os.system(cmd)
