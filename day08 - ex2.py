#필요한 모듈 임포트
from urllib.request import urlopen
from bs4 import BeautifulSoup
from matplotlib import pyplot

url="http://class.gnu.ac.kr/~elsa1122/bd/ex2.html"

#HTTP요청

try :
    htmlObj = urlopen(url)

except :
    print("요청 오류~")
else:
    bsObj = BeautifulSoup(htmlObj,"lxml")
    print(bsObj)

    
# 학년 정보 모두 찾기
yearObj = bsObj.findAll("td", {"class", "td-year"})
print(yearObj)

#학년 별 인원 수 세기 
year_cnt = [0,0,0,0,0,0,0]
for year in yearObj :
    if year.getText() == "1학년" :
        year_cnt[0] += 1    
    elif year.getText()  == "2학년" :
        year_cnt[1] +=  1
    elif year.get_text() == "3학년" :
        year_cnt[2] +=  1
    elif year.get_text() == "4학년" :
        year_cnt[3] +=  1
    elif year.get_text() == "대학원" :
        year_cnt[4] +=  1
    elif year.get_text() == "일반인" :
        year_cnt[5] +=  1
    else :
        year_cnt[6] +=  1

            

print("1학년: %d 명" %year_cnt[0])
print("2학년: %d 명" %year_cnt[1])
print("3학년: %d 명" %year_cnt[2])
print("4학년: %d 명" %year_cnt[3])
print("대학원: %d 명" %year_cnt[4])
print("일반인: %d 명" %year_cnt[5])
print("기타: %d 명" %year_cnt[6])



# 그래프 그리기
xList = ["first-year", "second-year", "third-year", "fouth-year", "a graduate student", "non-student", "etc.."]

pyplot.bar(xList, year_cnt)
pyplot.xlabel("What grade are you in?")
pyplot.ylabel("How many people?")
pyplot.title("How many students per grade ??? ")
pyplot.show()


