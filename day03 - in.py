
# in 을 사용하여 문자열이나 리스트의 특정 요소의 존재여부 검사

#if(조건문)와 함께 사용
if  'o'  in  "I love gnu" :
    print("'I love gnu'에 'o'가 포함되어 있다.")
    

s  =  "I love gnu"
if  'v'  in  s :
    print("'I love gnu'에 'v'가 포함되어 있다.")
    


s_list = [10, 20,30, 40]
if 5 in s_list :
    print("리스트에 5가 포함되어 있다.")



#for(조건문)와 함께 사용
for  i  in  "아름다운 우리대학" :
    print(i)




hap =0
i =1

for  e  in  [10, 20, 30, 40, 50] :
    print("%d 번째 수는 %d"  %(i, e))
    i += 1    
    hap += e

print("총 합은 %d 이다.  " %hap)





#in 으로 딕셔너리의 요소에 반복 접근
dic = {'100번':'이점숙', '200번':'김은경', '300번':'박순화'}
for  k  in  dic :
    print(k,  dic[k])
