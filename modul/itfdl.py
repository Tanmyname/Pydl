import re
from yt_dlp import YoutubeDL
import os 
import sys
from colorama import Fore as x

def cek_url_platform(url):
    pola_platform = {
        "TikTok": r"https://(www\.)?tiktok\.com/|https://vm\.tiktok\.com/",
        "Facebook": r"https://(www\.)?facebook\.com/",
        "Instagram": r"https://(www\.)?instagram\.com/",
        "YouTube": r"https://(www\.)?youtube\.com/watch\?v=|https://youtu\.be/"
    }
    
    for platform, pola in pola_platform.items():
        if re.search(pola, url):
            return platform
    
    return "Invalid url"

def getvid():
    url = input("input url =>  ")
    platform = cek_url_platform(url)
    if platform == "Invalid url":
        print("Uknown Url eror :( ")
        getvid()

    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }

    print(f"Downloder Video from  {platform}")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Downlod Complete ✓ ")
    except Exception as e:
        print(f"Shomthing wrong :( {e}")
    back = input("\n\nBack to Home => [y/n] ")
    if back == 'y' or back == 'Y':
      if os.name == 'nt':
            now = os.getcwd()
            os.chdir(now)
            os.system('python main.py')
            sys.exit()
        else :
            now = os.getcwd()
            os.chdir(now)
            os.system('python3 main.py')
            sys.exit()
    else:
        print('bye')
