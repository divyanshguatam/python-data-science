from turtle import *
# hexagonal pattern
bgcolor ('black')
speed('fastest')
colors = ['red','purple','blue','green','yellow','orange']
for x in range(360):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    left(59)
mainloop()        
