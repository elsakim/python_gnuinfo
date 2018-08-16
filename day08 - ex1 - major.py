#goo.gl/E5qjoN
from urllib.request import urlopen
from bs4 import BeautifulSoup
from matplotlib import pyplot

url="http://class.gnu.ac.kr/~elsa1122/bd/ex1.html"

try :
    htmlObj = urlopen(url)

except :
    print("요청 오류 입니다.")

else :
    bsObj = BeautifulSoup(htmlObj,"lxml")
    print(bsObj)    #for check

    

partObj = bsObj.findAll("td", {"class": "td-part"})
#print(partObj) #for check

partname = []


for part in partObj:
    partname.append(part.getText())
    print(part.getText())

print("\n\n--- 수강생들의 소속학과 --------------------------------------")
print(partname)

part_freq = {}
for i in partname :
    part_freq.setdefault(i, 0)

for i in partname :
    part_freq[i] = part_freq[i] +1

print("\n\n----- 학과별 수강 인원 ------------------------------------")
print(part_freq)


xList=[];yList=[]

for i in part_freq:
    xList.append(i)
    yList.append(part_freq[i])
    
print("\n\n-----------------------------------------")
print(xList)
print(yList)


   
pyplot.bar(xList, yList)
pyplot.xlabel("Major")
pyplot.ylabel("The number of people")
pyplot.title("Distribution Summary By Department This Period Graph ")
pyplot.show()

