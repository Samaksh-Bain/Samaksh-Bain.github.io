import requests
from bs4 import BeautifulSoup

header='Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
URL= "https://www.raymourflanigan.com"
r=requests.get(URL)


print(r)

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())

with open("bobs.html", "w", encoding='utf-8') as file:
    file.write(str(soup))