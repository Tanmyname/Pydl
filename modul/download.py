import requests
import json

def download_videos_by_key(json_file, key):
    # Langkah 1: Buka file JSON dan baca data
    with open(json_file, "r") as file:
        data = json.load(file)

    # Langkah 2: Ambil daftar URL berdasarkan key
    urls = data.get(key, [])
    
    if not urls:
        print(f"Tidak ada URL yang ditemukan untuk key '{key}'.")
        return
    
    # Langkah 3: Download setiap URL di dalam key yang dipilih
    for index, url in enumerate(urls, start=1):
        file_name = f"{key}_video{index}.mp4"  # Nama file disesuaikan
        try:
            print(f"Mengunduh {file_name} dari {url}...")
            response = requests.get(url)
            response.raise_for_status()  # Memastikan tidak ada error pada request
            
            # Simpan file ke disk
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"{file_name} berhasil diunduh.")
        
        except requests.exceptions.RequestException as e:
            print(f"Gagal mengunduh {file_name} dari {url}: {e}")

# Contoh penggunaan fungsi
download_videos_by_key("yuru_camp.json", "eps1")
