# image_site_downloader.py
# Downloads all images from a given webpage URL.

import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


# Headers to simulate a real browser (helps avoid some blocks)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def pick_from_srcset(srcset: str) -> str:
    """
    Extracts one image URL from a srcset attribute.
    srcset example:
    "img-small.jpg 480w, img-medium.jpg 800w, img-large.jpg 1200w"
    This function selects the last candidate, which is usually the largest image.
    """
    candidates = [c.strip().split(" ")[0] for c in srcset.split(",") if c.strip()]
    return candidates[-1] if candidates else ""

def safe_filename_from_url(img_url: str, fallback_index: int) -> str:
    """
    Generates a safe filename from a URL.
    If no valid name exists, creates a fallback name.
    """
    parsed = urlparse(img_url)
    name = os.path.basename(parsed.path)

    # If filename is empty or has no extension, create a default one
    if not name or "." not in name:
        name = f"image_{fallback_index}.jpg"

    # Remove characters that may cause issues in filenames
    name = re.sub(r"[^a-zA-Z0-9._-]", "_", name)
    return name

def main() -> None:
    # Ask the user for a page URL
    url = input("Insert URL: ").strip()

    # Download the HTML page
    res = requests.get(url, headers=HEADERS, timeout=20)
    res.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(res.text, "html.parser")

    # Find all image elements
    images = soup.select("img")

    # Create a folder to store downloaded images
    os.makedirs("images", exist_ok=True)

    downloaded = 0

    # Process each image tag
    for i, img in enumerate(images, start=1):
        # Try to get src or srcset
        src = img.get("src", "").strip()
        srcset = img.get("srcset", "").strip()

        # If src is missing, attempt to extract from srcset
        if not src and srcset:
            src = pick_from_srcset(srcset)

        # Skip if no valid source found
        if not src:
            continue

        # Skip embedded or unsupported image sources
        if src.startswith("data:") or src.startswith("blob:"):
            continue

        # Convert relative URLs into absolute URLs
        img_url = urljoin(url, src)

        try:
            print(f"Downloading {img_url}")

            # Download the image file
            img_res = requests.get(img_url, headers=HEADERS, timeout=20)
            img_res.raise_for_status()

            # Generate a safe filename
            filename = safe_filename_from_url(img_url, i)
            out_path = os.path.join("images", filename)

            # Avoid overwriting files with the same name
            if os.path.exists(out_path):
                base, ext = os.path.splitext(filename)
                out_path = os.path.join("images", f"{base}_{i}{ext}")

            # Save the image to disk
            with open(out_path, "wb") as f:
                f.write(img_res.content)

            downloaded += 1

        except Exception as e:
            # Continue if an image fails to download
            print(f"Could not download {img_url}: {e}")

    print(f"Done. Downloaded {downloaded} images.")

if __name__ == "__main__":
    main()
