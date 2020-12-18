import piexif
from PIL import Image


def write_data_to_exif(data_path, image_path, new_name):
    data = open(data_path,"rb").read()

    zeroth_ifd = {piexif.ImageIFD.Software: data}

    exif_dict = {"0th":zeroth_ifd}
    exif_bytes = piexif.dump(exif_dict)
    im = Image.open(image_path)
    im.save(new_name, exif=exif_bytes)

def read_exif_data(image_path, data_save_name):
    exif_dict = piexif.load(image_path)
    w = open(data_save_name,"wb")
    w.write(exif_dict["0th"][piexif.ImageIFD.Software])

