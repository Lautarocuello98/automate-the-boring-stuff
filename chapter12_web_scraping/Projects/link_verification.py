# Link Verification Tool

# This script checks a web page for broken links.

# How it works:
# 1. The user enters a URL.
# 2. The script downloads the page HTML.
# 3. It extracts all <a href=""> links.
# 4. Each link is requested using HTTP.
# 5. If a link returns status code 404, it is reported as broken.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def main():
    # ask the user for a URL
    url = input("Enter a URL to scan: ").strip()

    try:
        # Download the page
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f'Error accessing the page: {e}')
        return
    
    # parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # find all anchor tags
    links = soup.find_all('a')

    print(f'\nChecking {len(links)} Links...\n')

    for link in links:
        href = link.get('href')

        # skip empty links or archors
        if not href or href.startswith('#'):
            continue


        # convert relative URLs to absolute URLs
        full_url = urljoin(url, href)

        try:
            # request the link
            link_response = requests.get(full_url, timeout=10)
        
            # check if the link is broken
            if link_response.status_code == 404:
                print(f"Broken link (404): {full_url}")

        except requests.RequestException:
            # skip links that fail to connect
            print(f'Could not check: {full_url}')

    print("\nScan complete.")

if __name__ == "__main__":
    main()