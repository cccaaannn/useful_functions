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


