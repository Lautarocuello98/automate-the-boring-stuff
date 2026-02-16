from PIL import Image

cat_im = Image.open('zophie.png')
cropped_im = cat_im.crop((335, 345, 565, 560))
cropped_im.save('cropped.png')