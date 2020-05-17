import os
import shutil


def __read_from_file(file_name):
    try:
        with open(file_name,'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except (OSError, IOError) as e:
        print(e)

def __write_to_file(to_write, file_name, write_mode="w"):
    try:
        with open(file_name,write_mode, encoding='utf-8') as file:
            for item in to_write:
                file.write(str(item))
                file.write("\n")
    except (OSError, IOError) as e:
        print(e)

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

def __copy_all_files_from_dir(src, dest):
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        shutil.copy(full_file_name, dest)

def __create_dir_if_not_exists(path):
    if(not os.path.exists(path)):
        os.makedirs(path)

def __separate_path_name_ext(full_file_path):
    file_path, file_name = os.path.split(full_file_path)
    file_name, file_extension = os.path.splitext(file_name)
    return file_path, file_name, file_extension





