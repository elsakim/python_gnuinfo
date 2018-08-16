from  urllib.request  import  urlopen
from urllib.error import HTTPError


try :
    htmlObj = urlopen("https://docs.python.org/3/library/urllib.html")
    htmlObj = urlopen("http://pythonscraping.com/pages/page1.html")
    htmlObj = urlopen("http://pythonscraping.com/pages/page.html") #오류발생



except HTTPError as e :
    print(e)

else:
    print(htmlObj)
    print(htmlObj.read())
