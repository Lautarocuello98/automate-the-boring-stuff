from PIL import Image

img = Image.open('zophie.png')
print(img.size)
width, height = img.size
print(width)
print(height)

print(img.filename)
print(img.format)

print(img.format_description)

img.save('zophie.jpg')