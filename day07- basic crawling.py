from urllib.request  import  urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/warandpeace.html"

try :
    htmlObj = urlopen(url)    
except  :
    print("제대로 요청이 안됩니다")                                         
else :

   # print(htmlObj.read())    #제대로 요청이 되었나 확인
    bsObj = BeautifulSoup(htmlObj, "lxml")
    print(bsObj)

nameList = bsObj.findAll('span', attrs = {"class" :"green"}) 
print('------------------------------------')
print(nameList)

for name in nameList :
        print(name.get_text())



princeText = bsObj.findAll(text = "the prince")

n = len(princeText)
print("the prince  "  + str(n) + "회 나타남")
print("-----------------------")

for  i  in princeText :
	print(i)

print("\n\n")
