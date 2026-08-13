import turtle


t=turtle.Turtle()
t.speed(0)
for i in range(500):
    t.fd(i)
    t.right(i)

turtle.done()