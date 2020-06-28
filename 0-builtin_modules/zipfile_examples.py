from zipfile import ZipFile

def zip_file(files):
    with ZipFile('sample2.zip', 'w') as zip_obj:
        for file in files:
            zip_obj.write(file)

def unzip_file(name):
    with ZipFile(name, 'r') as zip_obj:
        zip_obj.extractall("")


