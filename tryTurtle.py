import turtle

window = turtle.Screen()
tortuguita = turtle.Turtle()
turtle.color("Deep Sky Blue")
turtle.shape('turtle')

grados = 0


tortuguita.speed(10)
for x in range(1,50):
    for x in range(0,4):
        tortuguita.forward(200)
        tortuguita.left(105)
        tortuguita.left(grados + 10)

window.mainloop()
