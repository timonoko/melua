# -*- coding: utf-8 -*-
import os,json,time

while True:
    time.sleep(5*60)
    b=json.loads(os.popen("termux-wifi-connectioninfo").read())
    if b['ip'] == "192.168.1.213":
        os.system("termux-api-start")
        os.system("termux-wake-lock")
        a=json.loads(os.popen("termux-battery-status").read())
        print(a)
        p=a['percentage']
        s=a['status']
        cur=a['current']
        plug=a['plugged']
#        if plug=="UNPLUGGED": os.system('termux-tts-speak UNPLUGGED')
        if p<41:
            os.system('termux-tts-speak Battery critical')
            os.system('killall play')
  
