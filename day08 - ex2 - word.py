from urllib.request import urlopen
from bs4 import BeautifulSoup


url="http://class.gnu.ac.kr/~elsa1122/bd/ex2.html"

#HTTP요청

try :
    htmlObj = urlopen(url)

except :
    print("요청 오류~")
else:
    bsObj = BeautifulSoup(htmlObj,"lxml")
    print(bsObj)


print('\n---------findAll()을  사용하여  수강 동기 위치 탐색---- ')
motivateObj = bsObj.findAll("ul", {"class": "why"})
print(motivateObj)   #ul 태그를 포함한 리스트

print('\n---------getText()를 사용하여  문자 추출하여 문자열에 저장---- ')
motivateStr=""
for i in motivateObj:
    print(i.get_text())
    motivateStr +=  i.get_text() + " "
    #motivateStr.append(i.get_text())  #ul태그를 제외한 문자열
print(motivateStr)

print('\n--------- 필요 없는 문자 제거 --------------------')
motivateStr = motivateStr.replace(",","")
motivateStr = motivateStr.replace(".","")
print(motivateStr)

print('\n--------- 공백기준으로 문자 분리하기--------------------')
motivateSpl = motivateStr.split(" ")
print(motivateSpl )

#빈도수 계산하기
motivate_freq = {}
for word in motivateSpl :
    motivate_freq.setdefault(word, 0)
    motivate_freq[word] += 1

print('\n--------- 시각화를 위한 자료 구조 만들어 데이터 저장하기 --------------------')
xList=[]
yList=[]

for word in motivate_freq :
    if motivate_freq[word] > 2:
        xList.append(word)
        yList.append(motivate_freq[word])        
print(xList)
print(yList)
