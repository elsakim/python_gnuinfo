import turtle as t

colors = ["red", "purple", "blue", "yellow"]
t.bgcolor("black")

#t.speed(0)
t.width(3)
len = 10

while len < 200 :
    t.forward(len)
    t.right(89)
    t.pencolor(colors[len%4])   
    len += 5


