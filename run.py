import os 
colorama = 'pip install colorama'
pytubefix = 'pip install pytubefix'
requests = 'pip install requests'
yt_dlp = 'pip install yt-dlp'
if os.name == 'nt':
  os.system('cls')
  os.system(colorama)
  os.system(pytubefix)
  os.system(requests)
  os.system(yt_dlp)
else :
  os.system('sudo apt install python3')
  os.system('pkg install python3')
  os.system('clear')
  os.system(colorama)
  os.system(pytubefix)
  os.system(requests)
  os.system(yt_dlp)
  
  
