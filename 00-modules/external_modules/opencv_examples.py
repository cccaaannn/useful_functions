# pip install opecv-python

# opencv has a looooot more in it

import cv2

# read image
img_array = cv2.imread(image_path)
img_array = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# resize image
im = cv2.resize(im, (img_width, img_height))


# show image
cv2.imshow('image', img)
cv2.waitKey(0)



def flip_images(source_dir, save_dir, flip_option=1):
    """
    flip_option=0 Vertical
    flip_option=1 Horizontal
    flip_option=-1 Both
    """
    import cv2
    import os
    for index, img in enumerate(os.listdir(source_dir)):
        print(index)
        originalImage = cv2.imread(os.path.join(source_dir, img))
        flipHorizontal = cv2.flip(originalImage, flip_option)
        cv2.imwrite(os.path.join(save_dir, img), flipHorizontal)


