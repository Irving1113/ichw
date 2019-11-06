import turtle
import math

sun = turtle.Pen()
mercury = turtle.Pen()
venus = turtle.Pen()
earth = turtle.Pen()
mars = turtle.Pen()
jupiter = turtle.Pen()
saturn = turtle.Pen()
  
def ellipse(a,b,t,color):
    minAngle = (2*math.pi/360) * 360 / 50
    t.color(color)
    t.shape("circle") 
    if i == 0:
        t.penup()
        t.setpos(0,-b)
    else:
        t.pendown()
    nextPoint = [a*math.sin((i+1)*minAngle),-b*math.cos((i+1)*minAngle)]
    t.setpos(nextPoint)  
    
for i in range(10000):
    ellipse(0,0,sun,"yellow")
    ellipse(57,34,mercury,"blue")
    ellipse(108,65,venus,"green")
    ellipse(149,90,earth,"red")
    ellipse(227,136,mars,"black")
    ellipse(278,167,jupiter,"orange")
    ellipse(327,196,saturn,"brown")

if __name__ == '__main__':
    main()
