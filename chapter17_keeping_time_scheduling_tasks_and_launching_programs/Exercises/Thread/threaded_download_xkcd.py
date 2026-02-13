#! python3
# threaded_download_xkcd.py - Downloads XKCD comics using multiple threads.

import requests
import threading
import os
import bs4

# Create the folder where images will be saved (does nothing if it already exists).
os.makedirs('xkcd', exist_ok=True)


def download_xkcd(start_comic: int, end_comic: int) -> None:
    for url_number in range(start_comic, end_comic):

        # 1) Download the HTML page for the comic number.
        print(f'Downloading page https://xkcd.com/{url_number}')
        res = requests.get(f'https://xkcd.com/{url_number}', timeout=15)
        res.raise_for_status()  # Stop this thread if the request failed (404, 500, etc.)

        # 2) Parse the HTML so we can locate the comic image tag.
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # 3) Locate the <img> tag inside the #comic section.
        comic_elem = soup.select('#comic img')
        if not comic_elem:
            # Sometimes a page might not have the expected structure.
            print('Could not find comic image')
            continue

        # 4) Extract the image URL from the <img src="..."> attribute.
        comic_url = comic_elem[0].get('src')

        # 5) Normalize the URL (XKCD often uses //imgs.xkcd.com/...).
        if comic_url.startswith('//'):
            comic_url = 'https:' + comic_url
        elif comic_url.startswith('/'):
            comic_url = 'https://xkcd.com' + comic_url

        # 6) Build the local filename and skip if it was already downloaded.
        filename = os.path.join('xkcd', os.path.basename(comic_url))
        if os.path.exists(filename):
            print(f'Skipping already downloaded {filename}')
            continue

        # 7) Download the image bytes.
        print(f'Downloading image {comic_url}')
        res = requests.get(comic_url, timeout=30)
        res.raise_for_status()

        # 8) Save the image in chunks (good for big files).
        with open(filename, 'wb') as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)


# Main thread: create, start, and wait for worker threads 

download_threads = []

# Create 14 threads that each download 10 comics.
# i = 0, 10, 20, ..., 130
for i in range(0, 140, 10):

    # Each thread will download [start, end) (end is excluded).
    start = i
    end = i + 10

    # XKCD has no comic 0, so start from 1.
    if start == 0:
        start = 1

    # Create a new thread that runs download_xkcd(start, end).
    t = threading.Thread(target=download_xkcd, args=(start, end))

    # Keep track of the thread so we can join() later.
    download_threads.append(t)

    # Start running the thread immediately.
    t.start()

# Wait for every thread to finish before exiting the program.
for t in download_threads:
    t.join()

print('Done')
