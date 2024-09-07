import webbrowser
import random
import subprocess
import os

count = 1
url_list = ["https://www.youtube.com/watch?v=oE4yu2C3Vfg&list=PLlcvR9uyH6_WS3gtoJhjWG1v0MS71OoQG&index=3",
             "https://www.youtube.com/watch?v=oE4yu2C3Vfg&list=PLlcvR9uyH6_WS3gtoJhjWG1v0MS71OoQG&index=3"]

while count != 0:
    webbrowser.open(url_list[random.randint(0,1)])
    subprocess.Popen ("C://Windows//System32//calc.exe")
    count +=1
