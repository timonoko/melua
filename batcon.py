# -*- coding: utf-8 -*-
import os,json,time

while True:
  try:
    b=json.loads(os.popen("termux-wifi-connectioninfo").read())
    if b['ip'] == "192.168.1.213":
        os.system("termux-api-start")
        os.system("termux-wake-lock")
        a=json.loads(os.popen("termux-battery-status").read())
        print(a)
        p=a['percentage']
        s=a['status']
        cur=a['current']
        if p<31: os.system('termux-tts-speak battery')
        if p<50:
            os.system('curl 192.168.1.101/4/off')
            time.sleep(0.1)
            os.system('curl 192.168.1.101/ON')
            os.system('curl 192.168.1.101/4/on')
        elif p>50:
            os.system('curl 192.168.1.101/4/on')
            time.sleep(0.1)
            os.system('curl 192.168.1.101/OFF')
            os.system('curl 192.168.1.101/4/off')
        else:
            os.system('curl 192.168.1.101/4/on')
            if s=='CHARGING': time.sleep(10)
            else: time.sleep(1)
            os.system('curl 192.168.1.101/4/off')

    else:
        os.system('termux-tts-speak no wifi')
        print('No KOTIKONE')
    time.sleep(30)
  except: pass
  
