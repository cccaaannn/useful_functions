from bs4 import BeautifulSoup
import requests


class requests_template():
    def __init__(self):
        self.base_url = ""
        self.soup = BeautifulSoup(features="html.parser")
        
    def __get_url(self, url):
        raw_site = requests.get(url, verify=False).text
        self.soup = BeautifulSoup(raw_site, features="html.parser")



def request_with_random_proxies(URL):
    # proxy example https://free-proxy-list.net/
    import requests
    proxies = {'http': 'http://190.64.18.177:80'}
    response = requests.get(URL, proxies=proxies) 
    return response    


def request_with_random_agents(URL):
    import requests
    import random
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36'
    ]
    user_agent = random.choice(user_agents)
    headers = {'User-Agent': user_agent}
    response = requests.get(URL, headers=headers)
    print("Response: ", response.json()['headers']['User-Agent'])
    return response


# get ip
def get_ip():
    import requests 
    response = requests.get('http://httpbin.org/ip') 
    return response.json()['origin']


# get all links
def get_links(is_internal=False):
    links = []
    for a in soup.find_all('a'):
        link = a.get('href');
        if(is_internal):
            if(link.startswith('/')):
                links.append(link)
        else:
            links.append(link)


# get all mails
def get_mails(text):
    import re
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}"
    mails = re.findall(pattern, str(text)) 
    return mails