import  turtle  as  t
t.color("purple")

n = int(input("몇 각형을 그릴까요?"))
w = int(input("한 선의 길이는 얼마가 좋을까요?"))

t.clear()
t.begin_fill()

for  x  in range(n):
    t.forward(w)
    t.left(360/n)

t.end_fill() 
