from static.menu import colors
import time



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
                print(colors.red + "  Error!! No proxies found.")
                time.sleep(3)
                quit()
            else:
                print(f"  Loaded Proxies: {proxiescount}")
                return proxies


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
