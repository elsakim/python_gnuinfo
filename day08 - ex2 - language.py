from urllib.request import urlopen
from bs4 import BeautifulSoup

from matplotlib import pyplot
from matplotlib import font_manager, rc
import matplotlib 


url="http://class.gnu.ac.kr/~elsa1122/bd/ex2.html"

#HTTP요청

try :
    htmlObj = urlopen(url)

except :
    print("요청 오류~")
else:
    bsObj = BeautifulSoup(htmlObj,"lxml")
    #print(bsObj)

#배운 프로그래밍 언어 데이터 가져오기

langObj = bsObj.findAll("ul", {'id' : 'language'})

langstr = ""
for i in langObj :
    langstr += i.get_text()
#print(langstr)

#필요없는 문자열과, 문자 분할하기
langstr = langstr.strip()
langstr = langstr.replace('\n', ' ')
langstr = langstr.split(' ')
print(langstr)

#학과 빈도수
lang_freq={}
for i in langstr:
    lang_freq.setdefault(i, 0)
    lang_freq[i] += 1
    
for i in lang_freq :
    print(i," : ", lang_freq[i])



#시각화 자료구조 만들기
x = []
y = []

for  lang in lang_freq :
	x.append(lang)
	y.append(lang_freq[lang])


font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

pyplot.bar(x, y)
pyplot.xlabel(" 프로그래밍 언어 ")
pyplot.ylabel(" 빈도수 ")
pyplot.title(" 언어별 빈도수 ")

pyplot.show ()

