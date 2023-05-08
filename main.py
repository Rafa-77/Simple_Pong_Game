# Simple Pong
# by @Rafa-77

import winsound
import turtle
# Turtle es para principiantes, crea gráficos para juegos básicos
window = turtle.Screen()
window.title("Pong by @Rafa")
window.bgcolor("black")
# background color, el color normal es blanco
window.setup(width=800, height=600)
# este tamaño es el estandar, es decir, esta de este tamaño sin que lo especifiques
# la coordenada (0,0) esta en el centro
window.tracer(0)
# tracer hace que la ventana deje de actualizarse, asi que se necesita actualizar manualmente, eso hace que el juego sea un poco más rápido


# Score
score_a = 0
score_b = 0

# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
# speed of animation, 0=maximun
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=0.5)
# shapesize funciona como un multiplicador del tamaño estandar
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# Queremos separar el movimiento de la bola en movimientos en (x,y)
# dx = delta (x) = cambio en x, cada movimiento de la pelota es en n(x,y) pixeles
ball.dx = 0.3
ball.dy = -0.3
# para recrear el movimiento de la pelota, debemos hacerlo en el Main Game Loop

# Pen, poner el marcador
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
# penup sirve para no dibujar una linea cuando se mueva la lines
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
# Default score
pen.write("Player A: 0   Player B: 0", align="center",
          font=("Courier", 24, "normal"))

# funciones
# Queremos mover los paddle para arriba y abajo


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


# cada juego necesita un maingameloop,  aqui van casi todos los potatoes del juego
# Main Game Loop
while True:
    # cada vez que corre el Loop, actualiza la ventana
    window.update()

    # Mover la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Checar bordes
    # cuando llega a cierto punto que revote, para ello se fijo el tamaño de la pantalla (recordar que
    # el centro esta en medio, porlo que sera negativo hacia abajo)
    # ARIIBA Y ABAJO
    if ball.ycor() > 290:
        ball.sety(290)
        # voltear la direccion de la pelota, en delta (y)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        # voltear la direccion de la pelota, en delta (y)
        ball.dy *= -1

    # IZQUIERDA Y DERECHA
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(
            score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(
            score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 55 and ball.ycor() > paddle_b.ycor() - 55):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound(winsound.Beep(250, 35), winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 55 and ball.ycor() > paddle_a.ycor() - 55):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound(winsound.Beep(250, 35), winsound.SND_ASYNC)
