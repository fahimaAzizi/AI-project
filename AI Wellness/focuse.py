import time
import datetime
import ctypes
import sys
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    current_time = datetime.datetime.now().strftime("%H:%M")
    stop_time = input("Enter block end time (HH:MM): ")
    a =current_time.replace(":",".")
    a =float(a)
    b= stop_time.replace(":",".")
    b = float(b)
    focus_Time = round(focus_Time,3)


    host_path = r"C:\\Windows\\System32\\drivers\\etc\\hosts"
    redirect = "127.0.0.1"

    website_list = ["www.facebook.com", "facebook.com", "youtube.com", "www.youtube.com"]

    if current_time < stop_time:
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write(f"\n{redirect} {website}")
            print("WEBSITES ARE BLOCKED")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time >= stop_time:
            with open(host_path, "r+") as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
            print("WEBSITES ARE UNBLOCKED")
            file = open("focus.txt","a")
            file.write(f"{focus_Time}")
            file.close()
            break
        time.sleep(60)

else:
    # Request admin privileges
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
