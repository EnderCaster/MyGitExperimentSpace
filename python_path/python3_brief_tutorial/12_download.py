#!/usr/bin/env python3
#-*- utf-8 -*-
import requests
import os
import os.path

def download(url):
    req=requests.get(url)
    if req.status_code==404:
        print("no resource like this")
        return
    filename = url.split('/')[-1]
    with open(filename,'wb') as fobj:
        fobj.write(req.content)
    print("finish")

if __name__ == '__main__':
    url =input("url=")
    download(url)
