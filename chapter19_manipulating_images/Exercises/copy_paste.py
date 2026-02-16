from PIL import Image

cat_im = Image.open('zophie.png')
cat_copy_im = cat_im.copy()

face_im = cat_im.crop((335, 345, 565, 560))
cat_copy_im.paste(face_im, (0, 0))
cat_copy_im.paste(face_im, (400, 500))
cat_copy_im.save('pasted.png')

cat_im_width, cat_im_height = cat_im.size
face_im_width, face_im_height = face_im.size
cat_copy2_im = cat_im.copy()


for left in range(0, cat_im_width, face_im_width):
    for top in range(0, cat_im_height, face_im_height):
        print(left, top)
        cat_copy2_im.paste(face_im, (left, top))


cat_copy2_im.save('pasted2.png')