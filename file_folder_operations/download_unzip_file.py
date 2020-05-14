import urllib.request
import zipfile

def downloadfile(url,name,unzip=True):
    urllib.request.urlretrieve(url, name)
    if(unzip):
        with zipfile.ZipFile(name, 'r') as zip_ref:
            zip_ref.extractall("")