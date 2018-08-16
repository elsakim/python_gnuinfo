#requests 모듈 사용하기

import requests as rq

'''
# 1. GET 요청
url="http://class.gnu.ac.kr/~jslee"
rq.get(url) 



# 2. POST 요청
url="http://class.gnu.ac.kr/~jslee"
rq.post(url)




# 3. 응답값 확인하기
url = "http://class.gnu.ac.kr/~jslee"
result = rq.post(url) #응답객체가 반환되어짐




# 4. status_code - 응답 정보 확인
def url_chk(url):
    result = rq.post(url)

    print(result)
    r = result.status_code

    if r == 200:
        print("%s 요청 성공" %(url))
    elif r == 404 :
        print("%s 요청 실패" %(url))
    else:
        print("%s 알 수 없는 에러 : %s" %(url, r))


url_chk("http://class.gnu.ac.kr/~jslee")
url_chk("http://class.gnu.ac.kr/~jslee34")



# 5.응답객체에서 헤더를 가져오기
url = "http://class.gnu.ac.kr/~jslee"

result = rq.post(url)  
print(result.headers)




# 6. HTML 코드 보기
url = "http://class.gnu.ac.kr/~jslee"
#url = "http://www.naver.com"
#url = "http://www.google.com"
#url =  "http://www.gnu.ac.kr"
result = rq.post(url)

print(result.text)
print('\n')
print(result.content)
print('\n')
print(result.encoding)
'''


# 7. 데이터 요청하는 방법 - 쿼리스트링 이용

url = "http://class.gnu.ac.kr/~jslee"
insu={'id':'jslee', 'passwd':1234}

res = rq.get(url, params = insu)
print(res.url)


res = rq.post(url, params = insu)
print(res.url)

















