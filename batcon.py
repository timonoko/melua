import os,json,time

os.system('curl-silent 192.168.1.101/4/on')
time.sleep(1)
os.system('curl-silent 192.168.1.101/OFF')
os.system('curl-silent 192.168.1.101/4/off')

while True:
    b=json.loads(os.popen("termux-wifi-connectioninfo").read())
    if b['ip'] == "192.168.1.213":
        os.system("termux-api-start")
        os.system("termux-wake-lock")
        a=json.loads(os.popen("termux-battery-status").read())
        print(a)
        p=a['percentage']
        s=a['status']
        cur=a['current']
        if p<40:
          print('critical')
          if s=='DISCHARGING' :
            os.system('termux-tts-speak battery low')
        if p<50:
            print('lataus päälle')
            try:
                os.system('curl-silent 192.168.1.101/ON')
                os.system('curl-silent 192.168.1.101/4/on')
            except: pass
        if p>50:
            print('lataus pois')
            try:
                os.system('curl-silent 192.168.1.101/OFF')
                os.system('curl-silent 192.168.1.101/4/off')
            except: pass
    else:
        os.system('termux-tts-speak no wifi')
        print('No KOTIKONE')
    time.sleep(20)
  
