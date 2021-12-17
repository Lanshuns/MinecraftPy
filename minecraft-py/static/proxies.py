from static.menu import colors
import time
import requests
import os



def load_proxy(proxy_type):
    if proxy_type == 'proxyless':
        pass
    else:
        with open("proxies.txt","r+",encoding="utf8",errors="replace") as proxy_file:
            proxy_text = proxy_file.read()
            proxies = proxy_text.splitlines()

            proxies = list(dict.fromkeys(proxies))
            proxiescount = len(proxies)
            if proxiescount == 0:
                print(colors.red + " Error!! No proxies was found.")
                time.sleep(3)
                quit()
            else:
                log = colors.yellow +  f" [+] Loaded Proxies: {proxiescount}"
                return proxies,proxiescount,log


def scrape_proxies(proxy_type: str):
    url = f"https://api.proxyscrape.com/v2/?request=getproxies&protocol={proxy_type}&country=all&anonymity=all"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
    try:
        rsp = requests.get(url, headers=headers, timeout=5)
    except Exception:
        print(colors.red + " Something went wrong while scrapping proxies, please retry again!")
        time.sleep(3)
        quit()

    proxylist = rsp.text
    proxylist = proxylist.splitlines()
    filterr = list(dict.fromkeys(proxylist))
    proxiescount = len(proxylist)
    log = colors.yellow + f" [+] Scrapid Proxies: {proxiescount}"
    return proxylist,proxiescount,log


def requests_proxy(proxy,proxy_type):
    if proxy_type == 'proxyless':
        pass
    else:
        proxy_parts = proxy.split(":")
        if len(proxy_parts) == 2:
            proxy = {"http": f"{proxy_type}://{proxy_parts[0]}:{proxy_parts[1]}",
                    "https": f"{proxy_type}://{proxy_parts[0]}:{proxy_parts[1]}"}
            return proxy
        elif len(proxy_parts) == 4:
            proxy = {"http": f"{proxy_type}://{proxy_parts[2]}:{proxy_parts[3]}@{proxy_parts[0]}:{proxy_parts[1]}",
                    "https": f"{proxy_type}://{proxy_parts[2]}:{proxy_parts[3]}@{proxy_parts[0]}:{proxy_parts[1]}"}
            return proxy
        else:
            pass
