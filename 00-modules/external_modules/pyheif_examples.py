# pyheif does not works on windows
# pip install pyheif


def convert_heic_to_jpg(image_path):
    """tries to convert the heic image to jpg with pyheif and pillow (does not works on windows)"""
    try:
        # pyheif not works on windows so we try to import it
        import pyheif

        # create new path name
        file_name, _ = os.path.splitext(image_path)
        new_path = file_name + ".jpg"

        # convert and save the image
        heif_file = pyheif.read(image_path)
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
            )

        image.save(new_path, "JPEG")

        # remove old extension image
        os.remove(image_path)
        return 1, new_path
    except Exception as e:
        print(e)
        return 0, image_path