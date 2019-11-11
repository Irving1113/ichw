import turtle
import math

sun = turtle.Pen()
mercury = turtle.Pen()
venus = turtle.Pen()
earth = turtle.Pen()
mars = turtle.Pen()
jupiter = turtle.Pen()
saturn = turtle.Pen()

k = r = m = n = o = p = 0


def run(a, c, t, color, speed, angle):
    t.shape('circle')
    t.color(color)
    t.speed(speed)
    if i == 0:
        t.up()
        t.goto(a-c+111, 0)
    else:
        t.down()
    b = (a**2 - c**2)**(1/2)
    angle = angle+speed
    x = a*math.cos(math.radians(angle))-c+111
    y = b*math.sin(math.radians(angle))
    t.goto(x, y)


for i in range(10000):
    run(0, 0, sun, 'yellow', 0, 0)
    run(57, 11, mercury, 'blue', 15, k)
    run(108, 31, venus, 'green', 12, r)
    run(149, 54, earth, 'red', 9, m)
    run(227, 97, mars, 'black', 4, n)
    run(278, 132, jupiter, 'orange', 3, o)
    run(327, 177, saturn, 'brown', 1, p)
    k = k+15
    r = r+12
    m = m+9
    n = n+4
    o = o+3
    p = p+1

if __name__ == '__main__':
    main()
