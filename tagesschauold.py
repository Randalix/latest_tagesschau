#!/usr/bin/env python3
import requests
import socket
from time import sleep
import os
import re
import sys
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")
if len(sys.argv) > 1: 
    player = sys.argv[1]
else:
    player = "castnow"

url = "https://www.tagesschau.de/multimedia/"
qualities = ["xl", "l", "m", "s"]
quality = qualities[0]
legit_types = [5300, 2000, 2600, 3000, 3300, 2700, 3700, 4700,1720, 3600]
pattern = re.compile(
        rf"https://download\.media\.tagesschau\.de/video/\d\d\d\d/\d\d\d\d/TV-\d\d\d\d\d\d\d\d-\d\d\d\d-\d\d00\.web{quality}\.h264\.mp4"
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
    mp4s = [mp4.group(0) for mp4 in matches]
    return mp4s


def get_valid_shows(mp4s):
    shows = []
    for mp4 in mp4s:
        type = int(mp4[-19:-15])
        for legit in legit_types:
            if type == legit:
                shows.append(mp4)
    return shows

def get_latest(shows):
    for show in shows:
        print(show)
    return  sorted(shows)[-1]


wait_till_online()
mp4s = get_all_mp4()
shows = get_valid_shows(mp4s)
url = get_latest(shows)
cmd = f"{player} {url}"
print(cmd)
os.system(cmd)
