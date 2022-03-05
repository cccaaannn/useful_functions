# https://github.com/torpyorg/torpy


from torpy.http.requests import tor_requests_session

with tor_requests_session() as s:
    link = "http://httpbin.org/ip"
    res = s.get(link)
    print(res.json()['origin'])


