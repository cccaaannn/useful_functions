# download with urllib request
import urllib.request

def download_file_request(url, download_path, replace_name=None):
    if(replace_name):
        downloaded_file_name = replace_name
    else:
        downloaded_file_name = url.split('/')[-1]

    downloaded_file_name_and_path = os.path.join(download_path, downloaded_file_name)
    try:
        urllib.request.urlretrieve(url, downloaded_file_name_and_path)
    except Exception as e:
        print(e, "download error")


# download with requests
import requests
import shutil
import os

def download_file_requests(url, download_path, replace_name=None):
    if(replace_name):
        downloaded_file_name = replace_name
    else:
        downloaded_file_name = url.split('/')[-1]

    downloaded_file_name_and_path = os.path.join(download_path, downloaded_file_name)
    try:
        with requests.get(url, stream=True) as req:
            with open(downloaded_file_name_and_path, 'wb') as file:
                shutil.copyfileobj(req.raw, file)
    except Exception as e:
        print(e, "download error")
