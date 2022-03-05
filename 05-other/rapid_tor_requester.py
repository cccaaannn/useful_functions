from torpy.http.requests import tor_requests_session
import concurrent.futures

class tor_requester():
    def __init__(self, URLs):
        self.URLs = URLs

    def __make_tor_request(self):
        with tor_requests_session() as s:
            def get_link(link):
                res = s.get(link)
                print(res.json()['origin'])

            with concurrent.futures.ThreadPoolExecutor(max_workers=self.request_per_connection) as executor:
                results = executor.map(get_link, self.URLs)

    def request(self, request_per_connection=3, threads=5):
        self.request_per_connection = request_per_connection
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            for _ in range(threads):
                executor.submit(self.__make_tor_request)



links = ["http://httpbin.org/ip"] * 3

tr = tor_requester(links)

tr.request()

