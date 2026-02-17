#! python3
# identifying_photo_folders.py - Walk through a directory tree and print folders that are likely "photo folders".
# A folder is considered a photo folder if more than half of its files are photos.

import os
from pathlib import Path
from PIL import Image  

for foldername, subfolders, filenames in os.walk(r"C:\\"):
    num_photo_files = 0
    num_non_photo_files = 0
    folder_path = Path(foldername)

    for filename in filenames:
        if not filename.lower().endswith(('.png', '.jpg')):
            num_non_photo_files += 1
            continue

        file_path = folder_path / filename

        # Open image file using pilow
        try:
            with Image.open(file_path) as im:
                width, height = im.size
        except:
            num_non_photo_files += 1
            continue
        
        # Check if width & height are larger than 500
        if width <= 500 or height <= 500:
            num_non_photo_files += 1
            continue
        num_photo_files += 1

    total_files = num_photo_files + num_non_photo_files
    if total_files == 0:
        continue
        
    if num_photo_files > total_files / 2:
        print(f"the folder {foldername} is a photo folder")
        

    
