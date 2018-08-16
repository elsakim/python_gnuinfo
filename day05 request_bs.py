import requests
from bs4 import BeautifulSoup
import json
import os

response = requests.get('http://class.gnu.ac.kr/~jslee/')

htmlObj=response.content
#print(htmlObj)
#---------------------------------------------------
bsObj = BeautifulSoup(htmlObj, 'html.parser')
print(bsObj)    #html과 함께 출력
#print(bsObj.text)    #문서의 내용만 출력


#----- <a> 태그만 추출 ----------------------------------------------
listObj =bsObj.select('body > a')
#print(listObj)


#----- 추출한 정보 딕셔너리에 담기  -----------------------------
dictObj = {}   #빈 딕셔너리 만들기
for i in listObj:
    dictObj[i.text] = i.get('href')
print(dictObj)       
'''
for i in dictObj.keys():
    print(i, ":" ,dictObj[i])

'''


#----- json로 딕셔너리 저장하기  -----------------------------
with open(os.path.join('result.json'), 'w+') as json_file :
     json.dump(dictObj, json_file)
