#합격/불합격 판단
score = int(input("성적을 입력하시오: "))

if score >= 60:
	print("합격입니다.")
else:
	print("불합격입니다.")



#홀수/짝수 판단
num = int(input("정수를 입력하시오: "))

if num % 2 == 0 :
	print("짝수입니다.")
else:
	print("홀수입니다.")



#양수, 0, 음수 판단하기
while True :
    n = input("정수를 입력하세요")
    
    if n == "Q" or n =="q" :
        break
    
    n = int(n)

    if n >0 :
            print("양수 \n")
    elif n == 0 :
            print("0 \n")
    else :
            print("음수 \n")
    
    
