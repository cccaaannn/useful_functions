from PIL import Image
import shutil
import os


def __create_dir_if_not_exists(path):
    if(not os.path.exists(path)):
        os.makedirs(path)

def __copy_all_files_from_dir(src, dest):
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        shutil.copy(full_file_name, dest)

def __separate_path_name_ext(full_file_path):
    file_path, file_name = os.path.split(full_file_path)
    file_name, file_extension = os.path.splitext(file_name)
    return file_path, file_name, file_extension

def __create_unique_file_name(file_path, before_number="(", after_number=")"):
    temp_file_path = file_path
    file_name_counter = 1
    if(os.path.isfile(temp_file_path)):
        while(True):
            save_path, temp_file_name = os.path.split(temp_file_path)
            temp_file_name, temp_file_extension = os.path.splitext(temp_file_name)
            temp_file_name = "{0}{1}{2}{3}{4}".format(temp_file_name, before_number, file_name_counter, after_number, temp_file_extension)
            temp_file_path = os.path.join(save_path, temp_file_name)
            file_name_counter += 1
            if(os.path.isfile(temp_file_path)):
                temp_file_path = file_path
            else:
                file_path = temp_file_path
                break

    return file_path


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


