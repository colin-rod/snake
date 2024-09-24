from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]

segments =[]
game_is_on = True

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)
    new_segment.penup()
    segments.append(new_segment)

screen.update()

while game_is_on:
    for seg in segments:
        seg.forward(20)


screen.exitonclick()