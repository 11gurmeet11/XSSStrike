#!/usr/bin/env python

import sys
import requests
import threading
from colorama import Fore, Back, Style
import time


print(
        Fore.YELLOW +
         """
   ____  _______ _______  _________ .___________.___________.___________  
  / __ \ \_   ___ \\      \ \_   ___ \|           |           |   ____\__ \ 
 / /_/ / /    \  \/|   |   \/    \  \/|   .--.  |   .--.  |  |__    ) |
 \____ \ \     \___|   |___|\     \___|   |  |  |   |  |  |   __/   / __ |
/_____/  \______  /\______  /\______  /___|  |__|___|  |__|__|     (____  /
               \/        \/        \/                          \/     \/ 
   ________.__             __            
  /  _____/|__| ____  _____/  |_  ____    
 /   \  ___|  |/ __ \|  __ \   __\/ __ \   
 \    \_\  \  \  ___/|  | \/|  | \  ___/   
  \______  /__|\___  >__|   |__|  \___  >  
         \/        \/                 \/   

          ⚔️ XSSStrike - Fast Cross-Site Scripting Scanner ⚔️

                                         
        """ + Fore.RESET)

print()
print()

file = open(sys.argv[1],'r')
payloads = open('payloads.txt','r')
def Send_req(url,payload):
    time.sleep(0.15)
    #while url[-1] != '=':
     #   url = url[:-1]
    url = url.replace("=",f"={payload}")

    try:

        res = requests.get(url)
        if payload in res.text:
           print(Fore.GREEN +'XSS Found   -->','   ' , f"{url}" + Fore.RESET)
           print(Fore.GREEN , f"{url}" + Fore.RESET, file=open('output.txt','w'))
           #print(Fore.GREEN +'XSS Found   -->','   ' , f"{url}" + Fore.RESET, file=open('output.txt','a'))
        else:
           print(Fore.RED +'XSS NOT Found   -->','   ' , f"{url}" + Fore.RESET)

    except Exception as e:
        pass
file = file.readlines()
for payload in payloads:
    for url in file:
        url = url.strip('\n')
        payload = payload.strip('\n')
        threading.Thread(target=Send_req,args=(url,payload,)).start()
