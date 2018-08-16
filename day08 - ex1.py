from urllib.request import urlopen
from bs4 import BeautifulSoup
from matplotlib import pyplot

url = "http://class.gnu.ac.kr/~elsa1122/bd/ex1.html"

try :
    htmlObj = urlopen(url)

except :
    print("요청 오류 입니다.")

else :
   bsObj = BeautifulSoup(htmlObj,"lxml")
#   print(bsObj)
 
# 학년별 신청인원수 출력
yearObj = bsObj.findAll("td", {"class": "td-year"})
print(yearObj)
  
year_cnt=[0,0,0,0,0,0,0]
for year in yearObj :
    if year.get_text() == "1학년" :
        year_cnt[0] +=  1
    elif year.get_text() == "2학년" :
        year_cnt[1] +=  1
    elif year.get_text() == "3학년" :
        year_cnt[2] +=  1
    elif year.get_text() == "4학년" :
        year_cnt[3] +=  1
    elif year.get_text() == "대학원" :
        year_cnt[4] +=  1
    elif year.get_text() == "일반인" :
        year_cnt[5] +=  1
    else:
        year_cnt[6] +=  1



print("1학년: %d 명" %year_cnt[0])
print("2학년: %d 명" %year_cnt[1])
print("3학년: %d 명" %year_cnt[2])
print("4학년: %d 명" %year_cnt[3])
print("대학원: %d 명" %year_cnt[4])
print("일반인: %d 명" %year_cnt[5])
print("기타: %d 명" %year_cnt[6])


xList= ["first \n year", "sencond \n year", "third \n year", "foutrh \n year", "a graduate \n student", "non \n student", "etc.."]
pyplot.bar(xList, year_cnt)
pyplot.xlabel("What grade are you in?")
pyplot.ylabel("How many people?")
pyplot.title("How many students per grade ??? ")
pyplot.show()

















