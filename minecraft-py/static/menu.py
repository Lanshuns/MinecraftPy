import os


class colors:
    green = "\u001b[32;1m" + "\033[1m"
    yellow = "\u001b[33;1m" + "\033[1m"
    red = "\u001b[31;1m" + "\033[1m"
    normal = "\u001b[0m" + "\033[1m"
    cyan = "\u001b[36m" + "\033[1m"
    magenta = "\u001b[35m" + "\033[1m"
    blue = "\u001B[34m" + "\033[1m"


def main_menu():
    title = print("""

            \u001b[0m\033[1m███╗   ███╗██╗███╗   ██╗███████╗ ██████╗██████╗  █████╗ ███████╗████████╗    \u001B[34m██████╗ \u001b[33;1m██╗   ██╗
            \u001b[0m\033[1m████╗ ████║██║████╗  ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝    \u001B[34m██╔══██╗\u001b[33;1m╚██╗ ██╔╝
            \u001b[0m\033[1m██╔████╔██║██║██╔██╗ ██║█████╗  ██║     ██████╔╝███████║█████╗     ██║       \u001B[34m██████╔╝ \u001b[33;1m╚████╔╝ 
            \u001b[0m\033[1m██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██║     ██╔══██╗██╔══██║██╔══╝     ██║       \u001B[34m██╔═══╝   \u001b[33;1m╚██╔╝  
            \u001b[0m\033[1m██║ ╚═╝ ██║██║██║ ╚████║███████╗╚██████╗██║  ██║██║  ██║██║        ██║       \u001B[34m██║        \u001b[33;1m██║   
            \u001b[0m\033[1m╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝       \u001B[34m╚═╝        \u001b[33;1m╚═╝    
        """)


def proxy_type():
    while 1:
        proxytype_input = (input(colors.normal + " [1]: Http/s\n [2]: Socks4\n [3]: Socks5\n > ")) 
        if proxytype_input.isdigit():
            proxytype_input = int(proxytype_input)
            if proxytype_input == 1:
                return 'http'
            elif proxytype_input == 2:
                return 'socks4'
            elif proxytype_input == 3:
                return 'socks5'
            else:
                print(colors.red + " Error!! Please choose one of available modes.")
        else:
            print(colors.red + " Error!! Please enter a digit.")

def timeout():
    while 1:
        num_timeout = (input(colors.normal + " Timeout(Secs): ")) 
        if num_timeout.isdigit():
            num_timeout = int(num_timeout)
            if num_timeout == 0:
                num_timeout = 1
            return num_timeout

        else:
            print(colors.red + " Error!! Please enter a digit.")

def threads():
    while 1:
        num_threads = (input(colors.normal + " Threads: ")) 
        if num_threads.isdigit():
            num_threads = int(num_threads)
            if num_threads == 0:
                print(colors.red + " Wrong Threads Number!! Please choose from 1 to 200.")
            elif num_threads <= 200:
                return num_threads
            else:
                print(colors.red + " Wrong Threads Number!! Max threads is 200.")
        else:
            print(colors.red + " Error!! Please enter a digit.")

def logs():
    while 1:
        Show_Logs = (input(colors.normal + " Show Logs:\n [1]: Yes\n [2]: No\n > ")) 
        if Show_Logs.isdigit():
            Show_Logs = int(Show_Logs)
            if Show_Logs == 1:
                return Show_Logs
            elif Show_Logs == 2:
                break
            else:
                print(colors.red + " Error!! Please choose one of available modes.")
        else:
            print(colors.red + " Error!! Please enter a digit.")
