#! python3
# download_xlcd.py - Downloads every single XKCD comic.

import requests
import os
import bs4

url = 'https://xkcd.com'              #starting url
os.makedirs('xkcd', exist_ok=True)    #store comics in ./xkcd

while not url.endswith('#'):
    # download the page.
    print('downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # find the URL of the comic image.
    comic_elem = soup.select('#comic img')

    if comic_elem == []:
        print('Could not find comic image.')
    else:
        comic_url = comic_elem[0].get("src")
        if comic_url.startswith("//"):
            comic_url = "https:" + comic_url
        # download the image
        print('Downloading image %s...' % (comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()
    
        # save the image to ./xkcd.
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    # get the prev button's url.
    prevlink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevlink.get('href')

print('Done')    