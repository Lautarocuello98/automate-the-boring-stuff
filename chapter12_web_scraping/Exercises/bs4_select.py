import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
print(elems[0].getText())
print(elems[0].attrs)
pElem = exampleSoup.select('p')
print(str(pElem[0]))
print(pElem[1].getText())