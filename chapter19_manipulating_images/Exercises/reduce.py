from PIL import Image

im = Image.open("fower.png")

# Reduce to fit inside 400x400 preserving aspect ratio
im.thumbnail((130, 130))

im.save("foto_reducida2.png")
