from multiprocessing import JoinableQueue as Queue


#Load text and replace errors with "spaces", wthout using error kwarg it will cause an exception
#Load Wordlist
def load_wordlist():
    with open("wordlist.txt","r",encoding="utf8",errors="replace") as wordlist_file:
        wordlist_text = wordlist_file.read()
        wordlists = wordlist_text.splitlines()
        
        #Remove dupes
        wordlists = list(dict.fromkeys(wordlists))
        wordlist_count = len(wordlists)
        print(f"  Loaded Wordlists: {wordlist_count}")
        return wordlists


#Loop the wordlists
def vail_wordlists(wordlista):
    q = Queue(maxsize=0)
    for wordlist in wordlista:
        valid_wordlist = False 
        try:
            #Only split the first instance of ":"
            username,password = wordlist.split(":",1)
            valid_wordlist = True
        except:
            #Some wordlists will not be valid and cause an exception if they can't be split or unpacked
            pass
        if valid_wordlist:
            q.put(wordlist.split(":",1))
    return q
