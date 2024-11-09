import yt_dlp

def download_facebook_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',  # Menentukan nama file output
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    url = input("Masukkan URL video Facebook: ")
    download_facebook_video(url)
