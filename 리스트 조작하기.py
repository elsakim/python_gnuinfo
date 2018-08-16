#리스트 데이터 처리하기


'''
#순차적인 정수 리스트 만들기

range1 = range(10)
range2 = range(10, 20)

print(list(range1))
print(list(range2))


#리스트에서 특정 요소의 위치 구하기
week=['월', '화', '수', '목', '금', '토', '일']
today = week[4]
pos = week.index(today)

print('오늘은 즐거운 불%s 입니다.' %today)
print('일주일 중 %s번째 요일 입니다.' %(pos+1))


#reverse( ) – 역순으로 만들기
listdata = list(range(5))
print('원본 리스트 : ', listdata)

listdata.reverse()
print('역순 리스트 : ', listdata)


#reversed( ) – 함수로역순으로 만들기
listdata = list(range(5))
print('원본 리스트 : ', listdata)

listdata2 =reversed(listdata)
print('역순 리스트 : ', list(listdata2))


# .append(값)  새로운 요소 추가
listdata = list(range(5))
print('원본 리스트 : ', listdata)

listdata.append(5)
listdata.append(6)
print('추가 후  : ', listdata)


# .pop()  - 마지막 요소 가져오면서(반환) 리스트에서 제거
listdata = list(range(5))
print('pop 이전 리스트 : ', listdata)

print(listdata.pop())
print('pop 이후  리스트 : ', listdata)



# .insert(값) - 특정 위치에 요소 삽입하기
listdata = ['사과', '배', '참외', '포도']
print('원본 리스트 : ', listdata)

listdata.insert(2, '수박')
print('변경된 리스트  : ', listdata)



# .del(값) - 특정 위치에 요소 제거하기
listdata = ['사과', '배', '참외', '포도']
print('원본 리스트 : ', listdata)

del listdata[0]
print('변경된 리스트  : ', listdata)


# .del(값) - 특정 요소 제거하기
listdata = ['사과', '배', '참외', '포도']
print('원본    리스트 : ', listdata)

listdata.remove("배")
print('변경된 리스트  : ', listdata)




#  .count(값)  - 특정  요소 개수 구하기

listdata = [1, 2, 2, 3, 3, 3, 4, 5, 6]
print('원본    리스트 : ', listdata)

cnt1=listdata.count(2)
cnt2=listdata.count(3)

print('2의 개수 = ', cnt1)
print('3의 개수 = ', cnt2)

 
# .sort()  -요소 정렬하기

namelist = ['이점숙', '김은경', '박순화']
print('정렬 전 :', namelist)

namelist.sort()
print('정렬 후 :', namelist)

# sorted() - 정렬, 원본 리스트 존재
namelist = ['이점숙', '김은경', '박순화']
print('정렬 전 :', namelist)

namelist1=sorted(namelist)
namelist2=sorted(namelist, reverse = True)
print('오름차순 정렬 :', namelist1)
print('내림차순 정렬 :', namelist2)



# enumerate  (인덱스 : 요소) 쌍의 리스트를 반환
weeklist=['월', '화', '수', '목', '금', '토', '일']
enu = list(enumerate(weeklist))
print(enu)

print('일주일 중')


for i, j in enumerate(weeklist) :
    print(' %d번째 요일 : %s요일' %(i+1, j))


# sum  - 모든 요소의 합 구하기

listdata = [1, 2, 2, 3, 3, 3, 4, 5, 6]
list_sum = sum(listdata)
print(list_sum)



# all , any – 리스트의 모든 요소가 참인지 확인하기 
listdata1 = [0, 1, 2, 3, 4]
listdata2 = [True, True, True]
listdata3 = ['', [], (), {}, None, False]

print(all(listdata1))
print(all(listdata2))
print(all(listdata3))

print(any(listdata1))
print(any(listdata2))
print(any(listdata3))




# join -  문자열이 요소인 리스트 인자를 받아 리스트의 모든 요소를 특정 문자열로 연결 

join_list=['2018년 05월 18일', '지금', '이','시간도', '지나가리라','집중하자']
j_str=' '

join_result=j_str.join(join_list)

print(join_result)






'''










