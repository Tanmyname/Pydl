import os 
from colorama import Fore 
from modul import ytdl,itfdl,pindl,anime
def cls():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
    

def main():
  cls()
  print(f"{Fore.YELLOW}-"*20)    
  print(f"{Fore.YELLOW}Welcome To {Fore.BLUE}Pydl {Fore.GREEN}>_")
  print(f"{Fore.BLUE}-"*20) 
  print(f"{Fore.YELLOW}Pydl A downloder program with Python\nList Program\n{Fore.GREEN}0 => To exit The Program\n1 => YTDL\n2 => PINDL \n3 => Anime-Sub id From muse\n4 => Anime From Ani-One Asia\n5 => All dl can dl vid from Yt-ig-tt-fb")
  print(f"{Fore.YELLOW}-"*20)  
  try :
    opsion = int(input(f"{Fore.BLUE}Select 0,1,2,3,4,5 => "))
    if opsion == 0:
      cls()
      print("Bye ")
    if opsion == 1:
        cls()
        print("Welcome in ytdl\n")
        ytdl.search()
    elif opsion == 2:
      cls()
      print("Welcome in pindl\n")
      pindl.runpindl()
    elif opsion == 3:
      cls()
      anime.muse_anime()
    elif opsion == 4:
      cls()
      anime.anione_anime()
    elif opsion == 5 :
      cls()
      itfdl.getvid()
  except ValueError:
    print(f"{Fore.RED}Invalid input plis input 1,2,3,4 not abjad or char ")
    main()
    

main()