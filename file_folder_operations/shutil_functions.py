import shutil



def zip_dir(dir_name):
    shutil.make_archive(dir_name+".zip", 'zip', dir_name)