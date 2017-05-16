import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile,'html.parser')
test = exampleSoup.select('.slogan.haha')
print(test[0].getText())