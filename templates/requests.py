from bs4 import BeautifulSoup
import requests


class requests_template():
    def __init__(self):
        self.base_url = ""
        self.soup = BeautifulSoup(features="html.parser")
        
    def __get_url(self, url):
        raw_site = requests.get(url, verify=False).text
        self.soup = BeautifulSoup(raw_site, features="html.parser")

