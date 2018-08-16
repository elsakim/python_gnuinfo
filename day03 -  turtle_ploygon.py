import  turtle  as  t
t.color("purple")

n = int(input("몇 각형을 그릴까요?"))

t.begin_fill()

for  x  in range(n):
    t.forward(50)
    t.left(360/n)

t.end_fill() 
