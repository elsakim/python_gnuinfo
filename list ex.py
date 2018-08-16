# 쉘 모드에서 순서대로 입력해서 확인해 보기
list_data=[1, 5,3,9,24,7,37]
list_data



list_data2 = list_data[:]   #리스트 복사
list_data2

sum(list_data)
min(list_data)
max(list_data)

list_data.index(24) #24의 인덱스 값 찾기

list_data.append(88) #리스트에 88가 추가
list_data


list_data.insert(0, 99) #리스트의 0번 인덱스에 99추가
list_data

list_data.pop() #리스트에서 데이터 하나 꺼내기
list_data

del list_data[0] #리스트의 0번 인덱스 삭제
list_data

list_data.remove(37) #리스트에서 37을 삭제
list_data

list_data.sort() #리스트 정렬, 원본변경됨
list_data


list_data.reverse() #리스트 역순정렬, 원본변경됨
list_data



li = sorted(list_data) #리스트 정렬, 원본유지, 정렬결과를 리턴
li



li2=reversed(li) #리스트 정렬, 원본유지, 정렬결과를 리턴
li2
print(li2)

list_data
list_data.append(7)   #7의 갯수 찾기 위해 추가
list_data


list_data.count(2)  #리스트에서 2의 갯수찾기
list_data.count(7)  #리스트에서 7의 갯수 찾기



join_list=['2018년', '5월',  '18일']
j_str= '###'

join_result=j_str.join(join_list)
print(join_result)

