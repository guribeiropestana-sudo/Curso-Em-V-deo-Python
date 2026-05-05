import turtle
import time

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("red")
t.width(2)

def desenhar_coracao(tamanho):
    t.clear()
    t.penup()
    t.goto(0, -tamanho)
    t.pendown()
    t.begin_fill()
    t.left(50)
    t.forward(tamanho * 2)
    t.circle(tamanho, 200)
    t.right(140)
    t.circle(tamanho, 200)
    t.forward(tamanho * 2)
    t.end_fill()
    t.setheading(0)

# animação (batimento)
while True:
    desenhar_coracao(50)
    time.sleep(0.3)
    desenhar_coracao(60)
    time.sleep(0.3)
