# https://piexif.readthedocs.io/en/latest/
# pip install piexif

import piexif
from PIL import Image

zeroth_ifd = {piexif.ImageIFD.Make: u"Canon",
              piexif.ImageIFD.XResolution: (96, 1),
              piexif.ImageIFD.YResolution: (96, 1),
              piexif.ImageIFD.Software: u"piexif"
              }
exif_ifd = {piexif.ExifIFD.DateTimeOriginal: u"2099:09:29 10:10:10",
            piexif.ExifIFD.LensMake: u"LensMake",
            piexif.ExifIFD.Sharpness: 65535,
            piexif.ExifIFD.LensSpecification: ((1, 1), (1, 1), (1, 1), (1, 1)),
            }
gps_ifd = {piexif.GPSIFD.GPSVersionID: (2, 0, 0, 0),
           piexif.GPSIFD.GPSAltitudeRef: 1,
           piexif.GPSIFD.GPSDateStamp: u"1999:99:99 99:99:99",
           }
first_ifd = {piexif.ImageIFD.Make: u"Canon",
             piexif.ImageIFD.XResolution: (40, 1),
             piexif.ImageIFD.YResolution: (40, 1),
             piexif.ImageIFD.Software: u"piexif"
             }

exif_dict = {"0th":zeroth_ifd, "Exif":exif_ifd, "GPS":gps_ifd, "1st":first_ifd}
exif_bytes = piexif.dump(exif_dict)
im = Image.open("00-modules/external_modules/piexif/image_examples/dog.jpg")
im.thumbnail((100, 100), Image.ANTIALIAS)
im.save("00-modules/external_modules/piexif/image_examples/out.jpg", exif=exif_bytes)
