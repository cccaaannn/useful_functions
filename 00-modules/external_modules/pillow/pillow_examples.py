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

# convert to jpg
def convert_to_jpg(image_path):
    """tries to convert the image to jpg with pillow"""
    try:
        # create new path name
        file_name, _ = os.path.splitext(image_path)
        new_path = file_name + ".jpg"
        
        # convert image
        image = Image.open(image_path).convert('RGB')
        image.save(new_path)

        # remove old extension image
        os.remove(image_path)
        return 1, new_path
    except Exception as e:
        print(e)
        return 0, image_path


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
