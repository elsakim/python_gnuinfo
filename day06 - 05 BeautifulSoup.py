from urllib.request import urlopen
from bs4 import BeautifulSoup

htmlObj = urlopen("http://pythonscraping.com/pages/_
                  page1.html")

bsObj = BeautifulSoup(htmlObj, "html.parser")

#bsObj = BeautifulSoup(htmlObj) #파서 미지정 : 기본은 'lxml'
#bsObj = BeautifulSoup(htmlObj,'lxml')

bsObj.find(
print(bsObj)
print(bsObj.find('h1'))

