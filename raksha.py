import turtle as t
t.bgcolor("black")
t.pensize(10)
t.speed(10)

for i in range(12):

    t.color("red")
    t.fillcolor("yellow")
    t.begin_fill()
    t.fd(200)
    t.circle(60,180)
    t.lt(30)
    t.fd(200)
    t.end_fill()

#highteckgirl
t.up()
t.goto(10,-30)
t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(125,220)
t.down()
t.pensize(30)
t.color("red")
t.fd(100)
t.circle(200,80)
#highteckgirl
t.up()
t.goto(-92,-205)
t.down()
t.lt(90)
t.fd(100)
t.circle(200,80)
t.up()
t.goto(40,-400)
t.down()
#Happy Rakshabandhan
t.color("red")
style = ('times new roma',12,'bold')
t.write('Happy Rakshabandhan',front=style,align='center')
t.hideturtle()
t.done()