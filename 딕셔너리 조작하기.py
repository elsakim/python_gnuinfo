# 딕셔너리 데이터 조작하기
# {키:값}의 쌍으로 구성
# 순서가 없음


'''
# 딕셔너리에 데이터 추가하기 - 방법 1
week_dic={}

week_dic['월']='Monday'
week_dic['화']='Tuesday'
week_dic['수']='Wednesday'

print(week_dic)



# 딕셔너리에 데이터 추가하기 - 방법 2
week_dic = {}
print(week_dic)

week_dic.setdefault('월','Monday')
print(week_dic)
week_dic.setdefault('화','Tuesday')
week_dic.setdefault('월','Mon')
print(week_dic)





# 딕셔너리에 데이터 추가하기 - 방법 3
week_list1=['월', '화','수','목','금','토','일']
week_list2=['Mon', 'Thu','Wed','Thu','Fri','Sat','Sun']
week_dic={}

for i,j in enumerate(week_list1):    
    val=week_list2[i]
    week_dic[j]=val


print(week_dic)


# 키:값 자료형 확인하기
dic1 = {'x':102, 'y':'string', 'z':[1,2,3,4], 'a':{1,2}, 'b':(3,4)}
dic2 = {1:'x', 2:'y'}

print(dic1)
print(dic2)



#딕셔너리 복사하기
dic1={'월':'Mon','화':'Thu', '수':'Wed'}
dic2 = dic1.copy()

print(dic1)
print(dic2)

'''
# 딕셔너리에 데이터 수정하기
week_dic={'월':'Mon','화':'Thu', '수':'Wed','목':'Thu', '금':'Fri', '토':'Sat', '일':'Sun'}

#week_dic['월']='Monday'

print(week_dic)
'''

# 딕셔너리에 특정 데이터 삭제하기
week_dic={'월':'Mon','화':'Thu', '수':'Wed','목':'Thu', '금':'Fri', '토':'Sat', '일':'Sun' }

del week_dic['월']

print(week_dic)




# 딕셔너리에 모든 요소  삭제하기
week_dic={'월':'Mon','화':'Thu', '수':'Wed','목':'Thu', '금':'Fri', '토':'Sat', '일':'Sun' }
print(week_dic)

week_dic.clear()
print(week_dic)



# 딕셔너리에서 키만 추출하기
week_dic={'월':'Mon','화':'Thu', '수':'Wed','목':'Thu', '금':'Fri', '토':'Sat', '일':'Sun' }

ks = week_dic.keys() #모든 키를 추출하여 딕셔너리 뷰 객체로 리턴
print(ks)

for i in ks:
    print('Key : %s \t Value : %s ' %(i, week_dic[i])) 




# 딕셔너리에서 값만 추출하기
dic={'1분기':505500,'2분기':610000, '3분기':620500,'4분기':650000}

vals = dic.values()
print(vals)

vals_list = list(vals)
vals_sum = sum(vals_list)
print('총 매출액 : %d ' %vals_sum)



# 딕셔너리에 모든 요소 추출하기

dic={'1분기':505500,'2분기':610000, '3분기':620500,'4분기':650000}

items = dic.items()
print(items)


for i in items :    
    print(i)


#리스트처럼 만들어 반환을 하지만 정확하게 리스트는 아니다.
#인덱싱이나 슬라이싱은 불가능
#print(items[0])     #오류발생 : 인덱싱 안되므로


#다음과 같이 변경
dic_to_list =list(items)  #리스트로 변경하기
print(dic_to_list[0])
    

# 딕셔너리에 특정 키가 존재하는지 확인하기

name_dic={'민준':13869,'지훈':13376,'현우':10739,'은경':10335}

k=input('이름을 입력하세요 : ')

if k in name_dic:
    print('이름이 <%s>인 출생아 수는 <%d>명입니다.' %(k, name_dic[k]))
else : 
    print('자료에는 <%s>인 이름은 존재하지 않습니다.' %k)
          



# 딕셔너리 정렬하기
name_dic={'민준':13869,'지훈':13376, '현우':10739, '은경':10335}
sort_1 = sorted(name_dic)   #name_dic를 오름차순 정렬하여 리스트로 리턴 
print(sort_1)       

def f1(x):
    return x[0]

def f2(x):
    return x[1]

#name_dic를 키 기준으로 오름차순 정렬
sort_2 = sorted(name_dic.items(), key=f1)  
print(sort_2)

#name_dic를 값 기준으로 오름차순정렬
sort_3 = sorted(name_dic.items(), key=f2)
print(sort_3)

#name_dic를 값 기준으로 내림차순정렬
sort_4 = sorted(name_dic.items(), key=f2, reverse=True)
print(sort_4)



#get() – 존재하지 않는 키의 값을 가져오려고 할 때 에러를 발생시키지 않음 
name_dic={'민준':13869,'지훈':13376, '현우':10739, '은경':10335}
#print(name_dic['은경']) #존재하는 키의 값에  접근
#print(name_dic['점숙']) #존재하지 않은 키의 값에 접근, 오류발생

print(name_dic.get('은경'))
print(name_dic.get('점숙'))
print(name_dic.get('점숙', 'default value'))


'''































