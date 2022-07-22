#!/usr/bin/env python3
import requests
import json
from bs4 import BeautifulSoup
import os
import socket
from time import sleep
import sys


def wait_till_online():
    try:
        host = socket.gethostbyname("tagesschau.de")
    except:
        sleep(1)
        print("offline")
        wait_till_online()

def get_latest(links):
    return  sorted(links)[-1]

def scrape_links(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # players = soup.find_all('div',  {"class": "ts-mediaplayer ts-mediaplayer--einszueins ts-mediaplayer--list"})

    players = soup.find_all('div',  {"class": "ts-mediaplayer"})
    links = []
    for player_item in players:
        attribs = player_item.attrs
        data = attribs["data-config"]
        try:
            title = json.loads(data)["mc"]["_title"]
            if "tsde" in title or title == "Ganze Sendung":
                if "Gebärdensprache" not in data:
                    links.append(json.loads(data)["mc"]['_mediaArray'][0]["_mediaStreamArray"][4]["_stream"])
        except KeyError:
            pass
    return links

player = "castnow"
if len(sys.argv) > 1: 
    player = sys.argv[1]
url = "https://www.tagesschau.de/multimedia/"
wait_till_online()
links = scrape_links(url)
url = get_latest(links)
cmd = f"{player} {url}"
os.system(cmd)
