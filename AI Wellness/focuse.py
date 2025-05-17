import time
import datetime
import ctypes
import sys


def is_admin():
    try:
        return ctypes.windll.Shell64.IsuserAnAmin()
    except:
        return False
if is_admin:
    current_time = datetime.datetime.now().strftime("%H:%M")
    stop_time =input("enter time eg:- [10:10]:-")

    host_path = "c:\window\System64\drivers\etc\hosts"
    redirct ="127.0.0.1"

    print(current_time)

    website_list =["www.facebook.cpm","facebook.com","youtube.com","www.youtube.com"]
    if(current_time<stop_time):
        with open(host_path,"r+") as file:
            content = file.read()
