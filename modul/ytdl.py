from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix import Search 
import os 
import sys 
from yt_dlp import YoutubeDL

def getvid(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Downlod Complete ✓ ")
    except Exception as e:
        print(f"Shomthing wrong :( {e}")


def dl(url):
  try:
    yt = YouTube(url, on_progress_callback = on_progress)
    print(yt.title)
    ys = yt.streams.get_highest_resolution()
    ys.download()
  except:
    print("eror restart dl ")
    getvid(url)
  
def mp4():
  url = input("\nInput url => ")
  dl(url)
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
  else :
    print("bye")

def mp3():
  url = input("\nInput url => ")
  try:
    yt = YouTube(url, on_progress_callback = on_progress)
    print(yt.title)
    ys = yt.streams.get_audio_only()
    ys.download(mp3=True)
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
    else :
      print("bye")
  except:
    print("Eror :( ")
    mp3()

def search():
  info = input("\nSearch from YouTube => ")
  results = Search(info)
  #info
  for index,video in enumerate(results.videos):
    print("-"*40)
    print(f"info {index} ")
    print(f'Title: {video.title}')
    print(f'URL: {video.watch_url}')
    print(f'Duration: {video.length} sec')
    print("-"*40)
    #limit 
    if index ==15:
      break 
  try :
    opsion = int(input("Get\n1 => Vid\n2 => Audio \n1,2 => "))
    if opsion == 1:
      mp4()
    elif opsion == 2:
      mp3()
  except ValueError :
    print("\nInvalid Input plis input number not abjad or char !")
    opsion = int(input("Get\n1 => Vid\n2 => Audio \n1,2 => "))
    if opsion == 1:
      mp4()
    elif opsion == 2:
      mp3()


def ytdl():
  print("-"*20)
  print("YTDL")
  print("-"*20)
  print("0 => Close program\n1 => Search Vid from yt\n2 => Download audio with your url\n3 => Download video whith your url")
  print("-"*20)
  try:
    opsion = int(input("input 0,1,2,3 => "))
    if opsion == 1:
      search()
      go = input("Back to main ? y/n ")
      if go == "y":
        ytdl()
    elif opsion == 2:
      mp3()
      go = input("Back to main ? y/n ")
      if go == "y":
        ytdl()
    elif opsion == 3:
      mp4()
    elif opsion == 0:
      pass
    else :
      print("Uknown opsion @#*#_# ? ")
      ytdl()
  except ValueError:
    print("Eror Plis input Number not abjad or char @$$@_&? ")
# ytdl()
