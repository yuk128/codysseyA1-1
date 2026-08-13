import turtle


t=turtle.Turtle()
t.speed(0)
for i in range(180*4):
    t.fd(i%180)
    t.right(i%180)

turtle.done()