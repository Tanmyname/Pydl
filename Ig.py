def igdl(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
    }
    try:
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
      print("\nDownload Complate :)")
    except Exception as e:
      print(f"Eror :( {e}")
      
def runigdl():
  cls()
  url = input("Input url => ")
  igdl(url)