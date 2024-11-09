from pytubefix import YouTube
from pytubefix.cli import on_progress
from yt_dlp import YoutubeDL
from pytubefix import Search
from colorama import Fore as x
import os 
import sys 

def rdl(url):
  yt = YouTube(url, on_progress_callback = on_progress)
  print(yt.title)
  ys = yt.streams.get_highest_resolution()
  ys.download()
  
def getanime(url):
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

def muse_anime():
  info = input(f"{x.GREEN}Search anime from Muse indonesia => ")
  try:
    eps = int(input("Get Eps 1-20 => "))
  except ValueError:
    print(f"\n\n{x.RED}Eror invalid input!\n")
    muse_anime()
  i = 0
  while True:
    i += 1
    results = Search(f"muse indonesia {info} Episode {i}")
    #info
    for index,video in enumerate(results.videos):
      print("-"*40)
      print(f"info{x.GREEN} {i} ")
      print(f'Title: {video.title}')
      print(f'URL: {video.watch_url}')
      print(f'Duration: {video.length} sec')
      url = video.watch_url
      print("-"*40)
      get = input(f"download Anime {info } Episode {i} [y/n] ? ")
      if get == "Y" or get == "y":
        try:
          getanime(url)
        except:
          print('Eror try again downloads')
          rdl(url)              
      else :
        break
      break
    if i >=eps:
      back = input("\n\nBack to Home => [y/n] ")
      if back == 'y' or back == 'Y':
        os.chdir('/sdcard/pydl')
        os.system('bash run.sh')
        sys.exit()
      else :
        break
  
def anione_anime():
  info = input(f"{x.GREEN}Search anime from Ani-One Asia => ")
  try:
    eps = int(input("Get Eps 1-20 => "))
  except ValueError:
    print(f"\n\n{x.RED}Eror invalid input!\n")
    anione_anime()
  i = 0
  while True:
    i += 1
    results = Search(f"Ani-One Asia {info} #{i}")
    #info
    for index,video in enumerate(results.videos):
      print("-"*40)
      print(f"info{x.GREEN} {i} ")
      print(f'Title: {video.title}')
      print(f'URL: {video.watch_url}')
      print(f'Duration: {video.length} sec')
      url = video.watch_url
      print("-"*40)
      get = input(f"download Anime {info } Episode {i} [y/n] ? ")
      if get == "Y" or get == "y":
         try:
            getanime(url)
          except:
            print('Eror try again downloads')
            rdl(url)              
      else :
        break
      break
    if i >=eps:
      back = input("Back to Home => [y/n] ")
      if back == 'y' or back == 'Y':
        os.chdir('/sdcard/pydl')
        os.system('bash run.sh')
        sys.exit()
      else :
        break
    
      
      

    
  
