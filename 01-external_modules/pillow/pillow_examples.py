# https://pillow.readthedocs.io/en/stable/

from PIL import Image, ImageFilter
import os


images_path = "01-external_modules/pillow/image_examples"
lena = "01-external_modules/pillow/image_examples/lena.jpg"
save_path = "01-external_modules/pillow/image_examples/thumb_images"


# load image
image = Image.open(lena)


# show
image.show()

# save
image.save(images_path + "/lena.png")

# rotate
image.rotate(90)

# resize
image.resize((300,300))

# thumbnail
image.thumbnail((100,50))

# convert grayscale
image.convert(mode="L")

# blur 
image.filter(ImageFilter.GaussianBlur(radius=2))



# convert all images to thumbnail
def make_thumbnail(images_path, save_path, max_size = (300, 300)):
    for image_name in os.listdir(images_path):
        if(image_name.endswith(".jpg")):
            iname, iext = os.path.splitext(image_name)
            new_image_name = iname + "_thumb" + iext
            old_path = os.path.join(images_path, image_name)
            new_path = os.path.join(save_path, new_image_name)

            image = Image.open(old_path)
            image.thumbnail(max_size)
            image.save(new_path)
