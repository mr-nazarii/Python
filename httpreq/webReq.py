from urllib import request , parse , error

from bs4 import BeautifulSoup

url = "https://www.nazariikubik.com/"
html = request.urlopen(url).read()
soup =  BeautifulSoup(html, "html.parser")

tags = soup("a")
for tag in tags:
    newTag = tag.get("href", None)
    if newTag == None : continue
    elif ":" not in newTag : continue
    else: print(newTag)
