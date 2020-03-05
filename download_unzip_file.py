def downloadfile(url,name,unzip=True):
    import urllib.request
    urllib.request.urlretrieve(url, name)
    
    if(unzip):
        import zipfile
        with zipfile.ZipFile(name, 'r') as zip_ref:
            zip_ref.extractall("")