import time
import os
from os import path


#TimeSamp
class times:
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")


#Write to text
class results:
    #All hits (Contains Secured & Unsecured)   
    def Hits(self):
        results_path = f"./Results/{times.timestamp}"
        file_name = "Hits.txt"
        if not os.path.exists(results_path):
            os.makedirs(results_path)
        file_path = path.join(results_path,file_name)
        with open(file_path,"a",errors="ingore") as f:
            f.write(self + "\n")
    #Free accounts    
    def Free(self):
        results_path = f"./Results/{times.timestamp}"
        file_name = "Free.txt"
        if not os.path.exists(results_path):
            os.makedirs(results_path)
        file_path = path.join(results_path,file_name)
        with open(file_path,"a",errors="ingore") as f:
            f.write(self + "\n")
    #Secured accounts
    def Secured(self):
        results_path = f"./Results/{times.timestamp}"
        file_name = "Secured.txt"
        if not os.path.exists(results_path):
            os.makedirs(results_path)
        file_path = path.join(results_path,file_name)
        with open(file_path,"a",errors="ingore") as f:
            f.write(self + "\n")
    #Unsecured accounts
    def Unsecured(self):
        results_path = f"./Results/{times.timestamp}"
        file_name = "Unsecured.txt"
        if not os.path.exists(results_path):
            os.makedirs(results_path)
        file_path = path.join(results_path,file_name)
        with open(file_path,"a",errors="ingore") as f:
            f.write(self + "\n")