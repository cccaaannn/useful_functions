from requests_html import HTMLSession

url = ""

session = HTMLSession()

r = session.get(url)

r.html.render()

fist_row = r.html.find('#element')

for element in fist_row:
    print(element.text)