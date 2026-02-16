#! python3 
# resize_and_add_logo.py - Resizes all images in current working directory to fit 
# in a 300x300 square, and adds catlogo.png to the lower-right corner.
import os
from PIL import Image

square_fit_size = 300
logo_filename = 'catlogo.png'

logo_im = Image.open(logo_filename)
logo_width, logo_height = logo_im.size

os.makedirs('with_logo', exist_ok=True)

for filename in os.listdir('.'):

    # Skip non-image files and the logo itself
    if (not filename.endswith(('.png', '.jpg', '.jpeg'))) or filename == logo_filename:
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

    # Add logo
    print(f'Adding logo to {filename}...')
    im.paste(logo_im, (width - logo_width, height - logo_height), logo_im)

    # Save
    im.save(os.path.join('with_logo', filename))
