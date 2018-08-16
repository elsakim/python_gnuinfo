from urllib.request import urlopen
from bs4 import BeautifulSoup

from matplotlib import pyplot
from matplotlib import font_manager, rc #한글지원 위해 추가
import matplotlib 


url="http://class.gnu.ac.kr/~elsa1122/bd/ex2.html"

#HTTP요청

try :
    htmlObj = urlopen(url)

except :
    print("요청 오류~")
else:
    bsObj = BeautifulSoup(htmlObj,"lxml")
    print(bsObj)

#학과 정보 찾기

majorObj = bsObj.findAll("td", {'class' : 'td-part'})

major_text=[]
for major in majorObj :
    major_text.append(major.get_text())
    print(major)


#학과 빈도수
major_freq={}
for i in major_text:
    major_freq.setdefault(i, 0)
    major_freq[i] += 1
    
for i in major_freq :
    print(i," : ", major_freq[i])



#시각화 자료구조 만들기
x = []
y = []

for  major  in major_freq :
	x.append(major)
	y.append(major_freq[major])


font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

pyplot.bar(x, y)
pyplot.xlabel(" 학  과 ")
pyplot.ylabel(" 빈도수 ")
pyplot.title(" 전공별 빈도수 ")

pyplot.show ()



