'''
#요청 방법 1
import urllib.request

#바이트 스트림을 전달 받음
htmlObj = urllib.request.urlopen("http://pythonscraping.com/pages/page1.html")

#요청 방법 2-1
import urllib.request as r
htmlObj = r.urlopen(" http://pythonscraping.com/pages/page1.html ")

#요청 방법 2-2
import urllib.request
r = urllib.request
htmlObj = r.urlopen(" http://pythonscraping.com/pages/page1.html ")


#요청 방법 4
from urllib.request import urlopen, Request
url ="http://pythonscraping.com/pages/page1.html"
req = Request(url)    #요청 객체 만들기
htmlObj = urlopen(req)   #요청 정보를 넘겨주고 페이지를 받아 옴
'''

#요청 방법 5 - 가장 간단한 방법
from urllib.request import urlopen
#htmlObj = urlopen(" http://pythonscraping.com/pages/page1.html ")
htmlObj = urlopen("https://docs.python.org/3/library/urllib.html")



print(htmlObj.status)  #응답코드

print(htmlObj)

status = htmlObj.getheaders()   #헤더정보 가져오기
for s in status :
    print(s)


print(htmlObj.read())

#read()로 읽었을 때 글자가 깨진다면
#인코딩 방법을 알아내어 디코딩 해주어야 함
#특히나, 한글...
print(htmlObj.read().decode('utf-8'))    
