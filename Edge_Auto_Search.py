import os
import time
import webbrowser
import random

#path of edege browser executabel file. (Change it according to your system)
edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

#Register the browser with edge name as mentioned below
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

#Add for loop for random searches according to number of searches required.
for eachSearch in range(0,35):
    subject=random.randint(999,99999) #used Random package randint method to generate random number for unique search as a subject.

    webbrowser.get('edge').open('https://www.bing.com/search?q='+str(subject)) #Prepare the search url along with random number(subject) to be search.

    time.sleep(1) #Give some time to complete the search.

time.sleep(5)
os.system("taskkill /im msedge.exe /f") #kill the browser after complete the search.
