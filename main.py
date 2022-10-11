from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_op = screen.textinput(title="Make a bet", prompt="Who will win the race? Enter a color?")
colors = ["red", "blue", "green","orange", "purple", "yellow"]
y_pos = [-100,-70,-40,-10,20,50]
all_turtle = []
for _ in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[_])
    tim.penup()
    tim.goto(x=-230,y=y_pos[_])
    all_turtle.append(tim)
if user_op:
    is_race = True

while is_race:
    for turtle in all_turtle:
        if turtle.xcor()> 230:
            is_race = False
            winner_color=turtle.pencolor()
            if winner_color==user_op:
                print(f"You win !. The Winner is {winner_color}.")
            else:
                print(f"You lost. The Winner is {winner_color}.")

        move= random.randint(0, 10)
        turtle.forward(move)
screen.exitonclick()