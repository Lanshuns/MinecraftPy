import os
import easygui


#Logs colors
class colors:
    green = "\u001b[32;1m" + "\033[1m"
    yellow = "\u001b[33;1m" + "\033[1m"
    red = "\u001b[31;1m" + "\033[1m"
    normal = "\u001b[0m" + "\033[1m"


#Title & main menu & about
class main_menu:
    os.system("mode con cols=140 lines=30")
    os.system("title Minecraft Simpler")

    about = """
    My Discord: StaiN#9677

    My GitHub: https://github.com/StaaiN

    My Bitcoin Address: 3JT4WFGqqrwvzN5hZzEXtC1pbjV9cMvZSn

    Awesome Python Master: https://github.com/Categorically
    """

    print(colors.normal + """

    ███╗   ███╗██╗███╗   ██╗███████╗ ██████╗██████╗  █████╗ ███████╗████████╗    ███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗██████╗ 
    ████╗ ████║██║████╗  ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝    ██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗
    ██╔████╔██║██║██╔██╗ ██║█████╗  ██║     ██████╔╝███████║█████╗     ██║       ███████╗██║██╔████╔██║██████╔╝██║     █████╗  ██████╔╝
    ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██║     ██╔══██╗██╔══██║██╔══╝     ██║       ╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██╗
    ██║ ╚═╝ ██║██║██║ ╚████║███████╗╚██████╗██║  ██║██║  ██║██║        ██║       ███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║
    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝       ╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝

    """)

    easygui.msgbox(msg=about, title='About', ok_button='Close', image=None, root=None)


#Threads input
def threads():
    while 1:
        num_threads = (input("  Threads: ")).lstrip('0')
        if num_threads.isdigit():
            num_threads = int(num_threads)
            if num_threads == 0:
                easygui.msgbox(msg="Wrong Threads Number!! Please choose from 1 to 200.", title='Error', ok_button='OK', image=None, root=None)
                num_threads = 1
            elif num_threads <= 200:
                return num_threads
            else:
                easygui.msgbox(msg="Wrong Threads Number!! Max threads is 200.", title='Error', ok_button='OK', image=None, root=None)
        else:
            easygui.msgbox(msg="Error!! Please enter a digit.", title='Error', ok_button='OK', image=None, root=None)

#Timeout input
def timeout():
    while 1:
        num_timeout = (input("  Timeout(Secs): ")).lstrip('0')
        if num_timeout.isdigit():
            num_timeout = int(num_timeout)
            return num_timeout

        else:
            easygui.msgbox(msg="Error!! Please enter a digit.", title='Error', ok_button='OK', image=None, root=None)

#Proxy Type input
def proxy_type():
    while 1:
        proxytype_input = (input("  Proxies Type:\n  [1]: Http/s\n  [2]: Socks4\n  [3]: Socks5\n  > ")).lstrip('0')
        if proxytype_input.isdigit():
            proxytype_input = int(proxytype_input)
            if proxytype_input == 1:
                proxytype = 'http'
            elif proxytype_input == 2:
                proxytype = 'socks4'
            elif proxytype_input == 3:
                proxytype = 'socks5'
            else:
                easygui.msgbox(msg="Error!! Please choose one of available modes.", title='Error', ok_button='OK', image=None, root=None)
            if proxytype_input <= 3:
                return proxytype
        else:
            easygui.msgbox(msg="Error!! Please enter a digit.", title='Error', ok_button='OK', image=None, root=None)

#Show Logs input
def logs():
    while 1:
        Show_Logs = (input("  Show Logs:\n  [1]: Yes\n  [2]: No\n  > ")).lstrip('0')
        if Show_Logs.isdigit():
            Show_Logs = int(Show_Logs)
            if Show_Logs <= 2:
                return Show_Logs
            else:
                easygui.msgbox(msg="Error!! Please choose one of available modes.", title='Error', ok_button='OK', image=None, root=None)
        else:
            easygui.msgbox(msg="Error!! Please enter a digit.", title='Error', ok_button='OK', image=None, root=None)
