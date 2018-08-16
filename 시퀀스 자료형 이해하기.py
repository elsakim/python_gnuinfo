# 시퀀스 자료의 인덱싱 이해하기
'''
strdata = 'Hello Python!'
listdata = [1,2, [1, 2, 3]]

print(strdata[6])
print(strdata[-2])
print(listdata[0])
print(listdata[-1])
print(listdata[2][-1])




# 시퀀스 자료의 슬라이싱  이해하기
strdata = 'Hello Python!'

print(strdata[1:5])
print(strdata[:7])
print(strdata[9:])
print(strdata[:-3])
print(strdata[-3:])
print(strdata[:])
print(strdata[::2])
  

# 시퀀스 자료의 연결  이해하기
strdata1 = 'Hello '
strdata2 = 'Python!'
strdata3 = 'Friend!'
listdata1=[1,2,3]
listdata2=[4,5,6]

print(strdata1 + strdata2)
print(strdata1 + strdata3)
print(listdata1 + listdata2)
 

# 시퀀스 자료의 반복   이해하기
strdata1 = '니가  '
strdata2 = '너무~ '
strdata3 = ' 보고싶어!'

print(strdata1 + strdata2 * 2 + strdata3 )



# 시퀀스 자료의 크기 이해하기
strdata1 = 'Hello Python!'
strdata2 = '안녕 파이썬~~~'
listdata=['a', 'b', 'c',strdata1, strdata2]

print(len(strdata1))
print(len(strdata2))
print(len(listdata))
print(len(listdata[3]))


# 시퀀스 자료의 멤버체크  이해하기
listdata = [1,2,3,4]
chk1 = 5 in listdata
chk2 = 3 in listdata
print(chk1);print(chk2)

strdata = 'Hello Python!'
chk3 = 'P' in strdata
chk4 = 'p' in strdata
print(chk3);print(chk4)
'''


#문자열 포맷팅 이해하기
str1='물' ; str2='공기'
num1 = 187.3 ; num2 = 75

print('%s과 %s 중에 어떤 것이 더 중요할까?' %(str1, str2))
print('저의 키는%fcm이고, 몸무게는 %dkg 입니다.'  %(num1, num2))
print('프로젝트의 진행률은 %d%%입니다.' %num2)








