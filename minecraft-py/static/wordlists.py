from multiprocessing import JoinableQueue as Queue
from static.menu import colors
import time



def load_wordlist():
    with open("wordlists.txt","r",encoding="utf8",errors="replace") as wordlist_file:
        wordlist_text = wordlist_file.read()
        wordlists = wordlist_text.splitlines()
        
        wordlists = list(dict.fromkeys(wordlists))
        wordlist_count = len(wordlists)
        if wordlist_count == 0:
            print(colors.red + " Error!! No wordlists was found.")
            time.sleep(3)
            quit()
        else :
            print(colors.yellow + f" [+] Loaded Wordlists: {wordlist_count}")
            return wordlists


def vail_wordlists(wordlists):
    q = Queue(maxsize=0)
    for wordlist in wordlists:
        valid_wordlist = False 
        try:
            username,password = wordlist.split(":",1)
            valid_wordlist = True
        except:
            username = wordlist
            valid_wordlist = True
        if valid_wordlist:
            q.put(wordlist.split(":",1))
    return q
