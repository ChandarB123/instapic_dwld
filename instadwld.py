import requests
from bs4 import BeautifulSoup
import shutil
import urllib3
import json


header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

username = input("Enter the username: ")
user_url = "https://www.instagram.com/" + username + "/?__a=1"



def profilepic(url):
    response = requests.get(url, headers=header).json()
    img_url = response['graphql']['user']['profile_pic_url_hd']
    return img_url


def posts(url):
    response = requests.get(url, headers=header).json()
    edges = response['graphql']['user']['edge_owner_to_timeline_media']['edges']
    i = 1
    for edge in edges: 
        img_url = edge['node']['display_url']
        resp = requests.get(img_url)
        fp = open("file{0}.jpg".format(i), "wb")
        fp.write(resp.content)
        fp.close()
        i = i + 1
