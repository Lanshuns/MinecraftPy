
def load_proxy():
    with open("proxies.txt","r",encoding="utf8",errors="replace") as proxy_file:
        proxy_text = proxy_file.read()
        proxies = proxy_text.splitlines()

        proxies = list(dict.fromkeys(proxies))
        proxiescount = len(proxies)
        print(f"  Loaded Proxies: {proxiescount}")
        return proxies


def requests_proxy(proxy,proxy_type):
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
