import sys

listdata = [4,6,3,4,3,4,3,4,4,4,3,4,4,2,4,1,1,2,4,3,5,3,3,3]
print('학년분포 : ', listdata)

cnt1=listdata.count(1)
cnt2=listdata.count(2)
cnt3=listdata.count(3)
cnt4=listdata.count(4)
cnt5=listdata.count(5)
cnt6=listdata.count(6)

print('1학년 = ', cnt1)
print('2학년 = ', cnt2)
print('3학년 = ', cnt3)
print('4학년 = ', cnt4)
print('졸업생 = ', cnt5)
print('일반인 =', cnt5,'\n\n')


print('=============== 학과 분포 ================')

major_list=[]
major_set=()

filereader = open('major.txt', 'r', encoding='utf-8' )
for row in filereader:
    row1=row.replace('\n', '')
    major_list.append(row1)
filereader.close()

major_set=set(major_list)

for i in major_set:
    print(i, ':', major_list.count(i) , '명')

print('\n\n')

print('=============== 사용언어  ================')
lang_list=[]
lang_set=()

filereader = open('lang.txt', 'r', encoding='utf-8' )
for row in filereader:
    row1=row.replace('\n','')
    row1=row.replace('\t','')
    lang_list.append(row1)
filereader.close()

lang_set=set(lang_list)

print(lang_set)
print('\n\n')
