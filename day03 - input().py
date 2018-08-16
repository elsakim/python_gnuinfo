'''
str = input("\n 점수를 입력하세요 : ")

if str.isdigit() :
    print("숫자 ")
else :
    print("문자")

while True:
    n= input("\n 점수를 입력하세요 : ")

    if n.isnumeric() != True :
        print("문자를 입력하셨습니다. 다시 입력하세요 ")
    else :
        print(n+100)
        break



#eval 함수를 활용하면 자동으로 정수는 정수로, 실수는 실수로 변환된다.
i = int(input("\n 정수를 입력하세요: "))
print(i)

e = eval(input("\n 숫자를 입력하세요: "))
print(e, type(e))
print(e, "+ 100 = ", e + 100)

e = eval(input("\n 숫자를 입력하세요: "))
print(e, type(e))
print(e, " + 1.1 = ", e + 1.1)
'''

#한번에 두 개의 입력을 받기 위해 split 함수를 사용한다.
#(공백으로 분리하는 것이 기본값)
s1, s2 = input('두 수를 입력하세요: ').split()

i1 = int(s1)
i2 = int(s2)

print('두 수의 합은 :', i1 + i2)
