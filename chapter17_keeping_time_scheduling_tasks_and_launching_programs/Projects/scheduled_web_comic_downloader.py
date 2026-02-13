#! python3
# scheduled_web_comic_downloader.py
# Periodically checks XKCD and downloads any new comics.

from __future__ import annotations

import os
import time
from pathlib import Path
from urllib.parse import urljoin
import threading

import requests
import bs4

# Base XKCD URL
base_url = "https://xkcd.com/"

# Folder where comics are saved
out_dir = Path("xkcd")
out_dir.mkdir(parents=True, exist_ok=True)

# File that stores the last downloaded comic ID
STATE_FILE = out_dir / "last.txt"

# How often to check for new comics (seconds)
CHECK_EVERY_SECONDS = 30 * 60  # 30 minutes

# Number of comics each thread downloads
CHUNK_SIZE = 10


def load_last_id() -> int:
    # Read last downloaded comic ID.
    if not STATE_FILE.exists():
        return 0
    try:
        return int(STATE_FILE.read_text(encoding="utf-8").strip())
    except ValueError:
        return 0


def save_last_id(comic_id: int) -> None:
     # Save last downloaded comic ID.
    STATE_FILE.write_text(str(comic_id), encoding="utf-8")


def get_latest_comic_id(session: requests.Session) -> int:
    # Get the latest comic ID from XKCD homepage.
    res = session.get(base_url, timeout=20)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    prev_link = soup.select_one('a[rel="prev"]')
    if not prev_link or not prev_link.get("href"):
        raise RuntimeError("Couldn't find rel='prev' link")

    prev_id = int(prev_link["href"].strip().strip("/"))
    return prev_id + 1  # latest = prev + 1


def get_comic_image_url(session: requests.Session, comic_id: int) -> str:
    # Get image URL for a specific comic.
    page_url = f"{base_url}{comic_id}/"
    res = session.get(page_url, timeout=20)

    if res.status_code == 404:
        raise RuntimeError(f"Comic #{comic_id} not found")

    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    img = soup.select_one("#comic img")

    if not img or not img.get("src"):
        raise RuntimeError(f"Image not found on {page_url}")

    return urljoin(base_url, img["src"].strip())


def download_image(session: requests.Session, img_url: str, out_path: Path) -> None:
    # Download image in chunks.
    with session.get(img_url, stream=True, timeout=30) as r:
        r.raise_for_status()
        with open(out_path, "wb") as f:
            for chunk in r.iter_content(1024 * 64):
                if chunk:
                    f.write(chunk)


def download_range(start_comic: int, end_comic: int) -> None:
    # Download a range of comics.
    with requests.Session() as session:
        session.headers.update({"User-Agent": "xkcd-auto-downloader"})

        for comic_id in range(start_comic, end_comic + 1):
            try:
                img_url = get_comic_image_url(session, comic_id)
            except Exception as e:
                print(f"Skipping #{comic_id}: {e}")
                continue

            filename = os.path.basename(img_url.split("?")[0])
            out_path = out_dir / f"{comic_id}_{filename}"

            # Skip if already downloaded
            if out_path.exists():
                print(f"Skipping existing {out_path.name}")
                continue

            print(f"Downloading #{comic_id}")
            try:
                download_image(session, img_url, out_path)
                print(f"Saved {out_path.name}")
            except Exception as e:
                print(f"Download failed #{comic_id}: {e}")


def run_check_and_download() -> None:
    #Check for new comics and download missing ones.
    with requests.Session() as session:
        latest_id = get_latest_comic_id(session)

    last_id = load_last_id()

    if latest_id <= last_id:
        print(f"No new comics. Latest #{latest_id}")
        return

    missing_start = last_id + 1
    missing_end = latest_id
    print(f"Downloading comics #{missing_start}..#{missing_end}")

    # Split work into thread chunks
    threads = []
    s = missing_start

    while s <= missing_end:
        e = min(s + CHUNK_SIZE - 1, missing_end)
        t = threading.Thread(target=download_range, args=(s, e))
        threads.append(t)
        t.start()
        s = e + 1

    # Wait for all threads
    for t in threads:
        t.join()

    # Update state after downloads
    save_last_id(missing_end)
    print("Cycle complete")


def main() -> None:
    # Main loop
    print("XKCD auto-downloader started")

    while True:
        try:
            print(time.strftime("%H:%M:%S"), "Checking...")
            run_check_and_download()
        except Exception as e:
            print("Unexpected error:", e)

        print(f"Sleeping {CHECK_EVERY_SECONDS} seconds\n")
        time.sleep(CHECK_EVERY_SECONDS)


if __name__ == "__main__":
    main()
