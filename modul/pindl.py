import requests
import os
import sys

def fetch_pinterest_images(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_urls = []
        try:
            pins = data['resource_response']['data']['results']
            for pin in pins:
                image_url = pin['images']['orig']['url']
                image_urls.append(image_url)
        except KeyError:
            print("Data JSON tidak memiliki format yang diharapkan.")
            return []

        return image_urls
    else:
        print(f"Gagal mengambil data, status code: {response.status_code}")
        return []

def download_image(image_url, output_dir):
    filename = os.path.join(output_dir, image_url.split('/')[-1])
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Gambar berhasil didownload: {filename}")
    else:
        print(f"Gagal mendownload gambar dari {image_url}, status code: {response.status_code}")

def download_images_from_pinterest(pinterest_url, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    image_urls = fetch_pinterest_images(pinterest_url)
    for image_url in image_urls:
        download_image(image_url, output_dir)



def runpindl():
  query = input("Download image => ")
  os.system("clear")
  pinterest_url = f"https://id.pinterest.com/resource/BaseSearchResource/get/?_=1619980301559&data=%7B%22options%22%3A%7B%22isPrefetch%22%3Afalse%2C%22query%22%3A%22${query}%22%2C%22scope%22%3A%22pins%22%2C%22no_fetch_context_on_resource%22%3Afalse%7D%2C%22context%22%3A%7B%7D%7D&source_url=%2Fsearch%2Fpins%2F%3Fq%3D{query}"
  output_dir = f'{query}'
  download_images_from_pinterest(pinterest_url, output_dir)
  back = input("\n\nBack to Home => [y/n] ")
  if back == 'y' or back == 'Y':
    os.chdir('/sdcard/pydl')
    os.system('bash run.sh')
    sys.exit()
  else :
    print("bye")
  