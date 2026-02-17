#! python3
# custom_seating_cards.py - Reads a list of guest names from guests.txt and generates a personalized 
# invitation card for each name. Each card includes:
# - A bordered card area
# - The guest's name centered on the card
# - Decorative flower images in two opposite corners

import os
from PIL import Image, ImageFont, ImageDraw

# Read all guest names from the text file
with open('guests.txt') as f:
    names = f.read().splitlines()

# Load the flower image and keep transparency
logo_im = Image.open('flower.png').convert("RGBA")

# Loop through each guest name and generate a card
for name in names:

    # Create a blank white image
    im = Image.new('RGBA', (400, 400), 'white')
    draw = ImageDraw.Draw(im)

    # Draw the rectangular border of the card using lines
    draw.line((20, 56, 380, 56), fill="black", width=2)   # top border
    draw.line((20, 344, 380, 344), fill="black", width=2) # bottom border
    draw.line((20, 56, 20, 344), fill="black", width=2)   # left border
    draw.line((380, 56, 380, 344), fill="black", width=2) # right border

    # Load font (make sure the font path exists)
    fonts_folder = 'FONT_FOLDER'
    arial_font = ImageFont.truetype(os.path.join(fonts_folder, 'arial.ttf'), 32)

    # Measure text size so it can be centered
    bbox = draw.textbbox((0, 0), name, font=arial_font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate centered position
    x = 200 - text_width // 2
    y = 200 - text_height // 2

    # Draw the guest name on the card
    draw.text((x, y), name, fill='gray', font=arial_font)

    # Paste decorative flowers in opposite corners
    # Top-left flower
    im.paste(logo_im, (30, 70), logo_im)

    # Bottom-right flower (calculated to stay inside the border)
    im.paste(
        logo_im,
        (380 - logo_im.width - 10, 344 - logo_im.height - 10),
        logo_im
    )

    # Save the finished card using the guest's name
    im.save(f'card_{name}.png')
