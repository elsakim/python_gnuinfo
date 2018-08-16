#로그인 프로그램
#허용된 아이디 :  jslee, jslee의  암호 : 1234
'''
# step 1
name = input("아이디를 입력하세요 : ")
    passwd = input("비번을 입력하세요 : ")

    if( name == "jslee"  and  passwd =="1234") :
            print("로그인 성공 \n")
    else :
            print("로그인 실패 \n")


# step 2            
while True :
    name = input("아이디를 입력하세요 : ")
    passwd = input("비번을 입력하세요 : ")

    if( name == "jslee"  and  passwd =="1234") :
            print("로그인 성공 \n")
    else :
            print("로그인 실패 \n")


# step 3
name=""
passwd=""

while(name != "jslee"  or  passwd !="1234") :       
    name = input("아이디를 입력하세요 : ")
    passwd = input("비번을 입력하세요 : ")

print("\n로그인 성공")

'''

# step 4
name=""
passwd=""
flag = 0 #로그인 정보가 제대로 입력되지 않은 상태

while(name != "jslee"  or  passwd !="1234") :
    if flag == 0 :
        print(" \n 로그인 정보를 입력하세요. ")
        flag =1
    else :
        print(" \n 로그인 실패!!! 다시 정보를 입력하세요. ")
        
    name = input("아이디를 입력하세요 : ")
    passwd = input("비번을 입력하세요 : ")

print("\n로그인 성공")














