#!/usr/bin/python
import sys
import os
from googleapiclient.discovery import build
import time

key = open(os.path.join(sys.path[0], './key.txt')).read().strip()
service = build('youtube', 'v3', developerKey=key)

while True:
    pewdiepiesubs = service.channels().list(
        part='statistics',
        id='UC-lHJZR3Gqxm24_Vd_AJ5Yw'
    ).execute()['items'][0]['statistics']['subscriberCount']

    tseriessubs = service.channels().list(
        part='statistics',
        id='UCq-Fj5jknLsUf-MWSy4_brA'
    ).execute()['items'][0]['statistics']['subscriberCount']
    Diff=(int(pewdiepiesubs) - int(tseriessubs))
    if Diff<=1000:
        print ('WARNING')
    print(fg.magenta + "PewDiePie is at " + str(pewdiepiesubs) + " subs")
    print(fg.red + "T-Series is at " + str(tseriessubs) + " subs")
    print(fg.white + "Sub gap is " + str(int(pewdiepiesubs) - int(tseriessubs)) + " subs")
    print("As of "+str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    del pewdiepiesubs
    del tseriessubs
    time.sleep(10)
