from PIL import Image

cat_im = Image.open('Zophie.png')
cat_im.rotate(90).save('rotated_90.png')
cat_im.rotate(180).save('rotated_180.png')
cat_im.rotate(270).save('rotated_270.png')

cat_im.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')

