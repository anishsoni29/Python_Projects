from turtle import Turtle, Screen

tim =  Turtle()
screen =  Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading =  tim.heading() +10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

#When putting fucntion in function there is no requirement of parenthesis in the next function.

screen.listen()
screen.onkey(key = "W", fun = move_forwards)
screen.onkey(key = "S", fun = move_backwards)
screen.onkey(key="A", fun= turn_left)
screen.onkey(key="D", fun= turn_right)
screen.onkey(key="C", fun= clear)
screen.exitonclick()

#to listen the keys: On key listeners are used

