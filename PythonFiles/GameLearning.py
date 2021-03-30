import turtle

window = turtle.Screen()
window.title("Game Test")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

#Paddle 1 (default sqaure 20 pixels)
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid = 5, stretch_len = 1)
paddleA.penup()
paddleA.goto(-350, 0)

#Paddle 2
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid = 5, stretch_len = 1)
paddleB.penup()
paddleB.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid = 5, stretch_len = 1)
ball.penup()
ball.goto(0, 0)

#Functions
def movePaddleAUP():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def movePaddleAUP():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

#Key binding
window.listen()
window.onkeypress(movePaddleAUP, "w")

#Main game loop
playing = True

while playing:
    window.update()