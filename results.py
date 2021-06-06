import time
import os
from os import path


#TimeSamp
class times:
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

#Write to text
class results:
    def Hits(self):
        results_path = f"./Results/{times.timestamp}"
        file_name = "Hits.txt"
        if not os.path.exists(results_path):
            os.makedirs(results_path)
        file_path = path.join(results_path,file_name)
        with open(file_path,"a",errors="ingore") as f:
            f.write(self + "\n") 
    def Free(self):
        results_path = f"./Results/{times.timestamp}"
        file_name = "Free.txt"
        if not os.path.exists(results_path):
            os.makedirs(results_path)
        file_path = path.join(results_path,file_name)
        with open(file_path,"a",errors="ingore") as f:
            f.write(self + "\n")
    def Secured(self):
        results_path = f"./Results/{times.timestamp}"
        file_name = "Secured.txt"
        if not os.path.exists(results_path):
            os.makedirs(results_path)
        file_path = path.join(results_path,file_name)
        with open(file_path,"a",errors="ingore") as f:
            f.write(self + "\n")

    def Unsecured(self):
        results_path = f"./Results/{times.timestamp}"
        file_name = "Unsecured.txt"
        if not os.path.exists(results_path):
            os.makedirs(results_path)
        file_path = path.join(results_path,file_name)
        with open(file_path,"a",errors="ingore") as f:
            f.write(self + "\n")
