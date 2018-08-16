#파이썬의 예외 처리 : try ~ except
'''
# step 1
try :
    a = "hello"
    print(a)
    print(a[10])
    print(a)

except :
     print("error 발생")



# step 2
try :
    a = 10
    b = 0  
    print(a)
    print(b)
    print(a/b)  

except :
    print("error 발생")

# step 3
try :
    a = 10
    b = 0
    c= "jslee"

    print(a)
    print(b)
#    print(a/b)
#    print(c[10])
    
except  ZeroDivisionError :
    print("ZeroDivisioError error 발생")

except  IndexError :
    print("IndexError error 발생")


else :
    print('try 영역이 정상적으로 실행됐을 때')
    
finally :
    print('최종적으로 무조건 실행되는 구문')




# step 4

while True :
    n = input("정수를 입력하세요")

    if n == "Q" or n =="q" :
        break

    try :    
        n = int(n)

    except ValueError :
        print("정수로 변환할 수 없습니다.")
        
    else :
        if n >0 :
            print("양수")
        elif n == 0 :
            print("0")
        else :
            print("음수")

'''

# step 5

while True :
    n1 = input("첫번째 정수를 입력하세요")

    if n1 == "Q" or n1 =="q" :
        break
    
    n2 = input("두번째정수를 입력하세요")    

    try :
         n1 = int(n1)
         n2 = int(n2)
         
         if n1 > n2 :
             print(n1, " / ", n2, " =  ", n1/n2 )
             
         elif  n2 > n1 :
             print(n2, " / ", n1, " =  ", n2/n1 )

         elif n1==n2 :
             print("두 수는 같으므로 나눈 결과는 1입니다.")
             
    except ValueError :
        print("정수로 변환할 수 없습니다.")

    except ZeroDivisionError :
        print("ZeroDivisioError error 발생") 
        
    else : 
        print("\n")
    finally :
        print("한번 더 실행해볼까요? ")
        
             

       



    
