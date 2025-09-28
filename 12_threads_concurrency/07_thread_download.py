import threading
import requests
import time

def download(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    # here want to show the progress of download
    print(f"Content length: {resp.headers}")
    # total_length = int(resp.headers.get())
    # downloaded = 0
    # for chunk in resp.iter_content(chunk_size=1024):
    #     downloaded += len(chunk)
    #     print(f"Downloading {url}: {downloaded / total_length * 100:.2f}%")
    print(f"Finished downloading from {url}, size: {len(resp.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"All downloads done in {end - start:.2f} seconds")