import turtle

# window
window = turtle.Screen()
window.title("Pong game")
window.bgcolor("black")
window.setup(width=800, height=600)  # classical low res
window.tracer(0)  # stops from updating so I update in while loop

# paddle a
paddle_a = turtle.Turtle()  # paddle object
paddle_a.speed(0)  # animation speed
paddle_a.shape("square")  # assign shape and color
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # by default it's 20x20 so we stretch it(multiply)
paddle_a.penup()  # don't draw line
paddle_a.goto(-350, 0)  # because left bound is 400 and 0 makes it start at center

# paddle b
paddle_b = turtle.Turtle()  # paddle object
paddle_b.speed(0)  # animation speed
paddle_b.shape("square")  # assign shape and color
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # by default it's 20x20 so we stretch it(multiply)
paddle_b.penup()  # don't draw line
paddle_b.goto(350, 0)  # because left bound is 400 and 0 makes it start at center
# ball
# paddle b
ball = turtle.Turtle()  # ball object
ball.speed(0)  # animation speed
ball.shape("square")  # assign shape and color
ball.color("white")
ball.penup()  # don't draw line
ball.goto(0, 0)  # start at center


# functions
def paddle_a_up():
    y = paddle_a.ycor()  # y coordinate
    y += 20  # goes up by 20 pixels
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()  # y coordinate
    y -= 20  # goes up by 20 pixels
    paddle_a.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")

# game loop
while True:
    window.update()
