#주민등록번호로 남/여 판단
'''
num = input("주민등록번호를 입력하세요 : ")

if num[7] == "1" :
    print("당신은 남자입니다.")
else :
    print("당신은 여자입니다.")



#num[7]이 1또는 2 외의 값을 갖는 경우 처리
num = input("주민등록번호를 입력하세요 : ")

if num[7] == "1" or num[7] == "3":
    print("당신은 남자입니다.")
elif num[7] == "2" or num[7] == "4":
    print("당신은 여자입니다.")
else :
    print("판단할 수 없습니다. 다시 입력하세요")
'''


#종료 조건 넣기, 주민등록번호 자릿수확인
while True:
    num = input("주민등록번호를 입력하세요[종료는 'Q' 또는 'q'] : ")

    if num == 'Q' or num =='q' :
        print("프로그램 종료")
        break

    if len(num) != 14 :
        print("길이가 맞지 않습니다. 다시입력하세요\n ")

    elif num[7] == "1" or num[7] == "3":
        print("당신은 남자입니다. \n")
        
    elif num[7] == "2" or num[7] == "4":
        print("당신은 여자입니다. \n")
        
    else :
        print("판단할 수 없습니다. 다시 입력하세요 \n")
