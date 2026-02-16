#! python3 
# resize_and_logo.py - (Remake) - Resizes all images in current working directory to fit 
# in a 300x300 square, and adds catlogo.png to the lower-right corner (only if the image is at least 2x the logo size).

import os
from PIL import Image

square_fit_size = 300
logo_filename = 'catlogo.png'

logo_im = Image.open(logo_filename)
logo_width, logo_height = logo_im.size

os.makedirs('with_logo', exist_ok=True)

for filename in os.listdir('.'):

    # Skip non-image files and the logo itself
    if (not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))) or filename.lower() == logo_filename:
        continue

    im = Image.open(filename)
    width, height = im.size

    # Resize if needed
    if width > square_fit_size or height > square_fit_size:

        if width > height:
            height = int((square_fit_size / width) * height)
            width = square_fit_size
        else:
            width = int((square_fit_size / height) * width)
            height = square_fit_size

        print(f'Resizing {filename}...')
        im = im.resize((width, height))

    # Recalculate size (important)
    width, height = im.size

    # Only add the logo if the image is at least 2x the logo in BOTH dimensions 
    if width < logo_width * 2 or height < logo_height * 2:
        print(f'skipping logo for {filename} (image too small).')
        continue

    # Add logo
    print(f'Adding logo to {filename}...')
    im.paste(logo_im, (width - logo_width, height - logo_height), logo_im)

    # Save
    im.save(os.path.join('with_logo', filename))   
