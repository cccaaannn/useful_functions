from selenium import webdriver
from selenium.webdriver.chrome.options import Options 


class requests_selenium():
    def __init__(self, driver_path, options = ["--headless","--no-sandbox","--disable-dev-shm-usage"]):
        self.base_url = ""
        self.driver_path = driver_path
        self.options = options
        self.__init_driver(self.driver_path, self.options)

    def __init_driver(self,driver_path, options):
        self.__set_driver_options(options)
        self.driver = webdriver.Chrome(executable_path=driver_path, options=self.chrome_options)

    def __set_driver_options(self, options):
        self.chrome_options = Options()  
        if(options):
            for option in options:
                self.chrome_options.add_argument(option)
        
    def __get_url(self, url):
        self.driver.get(url)

