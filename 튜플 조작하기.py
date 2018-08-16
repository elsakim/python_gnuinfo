# 튜플 -  ( )로 생성, 값을 수정하거나 삭제할 수 없음
'''
#인덱싱과 슬라이싱
t = (0, 1,2,3,4,5,6,7,8,9)

print(t)
print(t[5])
print(t[:5])
print(t[5:])
print(t[::2])



# 연결과 반복
t1 = ('역시', )
t2 = ('잘한다','~~~~')
t3 = ('화이팅', '!!!') 

print(t1 + t2 + t3 )
print(t2 * 2)
print(t3 * 3) 
print(t1 + t2*2 + t3*3)



# 튜플 풀기 - 튜플 내의 원소들은 할당 연산자의왼편에 변수들을 배치하여 개별 값들로 풀러낼 수 있다.
my_tuple =('kim', 'park','lee')
print(my_tuple)

t1, t2, t3 = my_tuple
print('t1 = ', t1)
print('t2 = ', t2)
print('t3 = ', t3)

t1, t2 = t2, t1
print('t1 = ', t1)
print('t2 = ', t2)



#튜플 <--> 리스트
my_tuple =('kim', 'park','lee')
print(my_tuple)

my_list = list(my_tuple)
print(my_list)

to_tuple = tuple(my_list)
print(to_tuple)





#set 조작하기
a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)  

print(a - b)                          

print(a | b)      # either a or b                     

print(a & b)      # both a and b                     

print(a ^ b)     # a or b but not both


     '''
