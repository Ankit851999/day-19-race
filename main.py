from turtle import Turtle,Screen
from random import randint
race_over = False
screen = Screen()
screen.setup(width=800, height=800)
user_bet = screen.textinput(title="Make your bet", prompt="which color will win the race enter: ").lower()
colour = ["red", "purple", "green", "blue", "yellow", "orange"]
turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour[i])
    new_turtle.penup()
    new_turtle.goto(x=-380, y=(-200+(i*50)))
    turtles.append(new_turtle)
if user_bet:
    race_over = True
while race_over:
    for turtle in turtles:
        turtle.forward(randint(1,10))
        if turtle.xcor() > 380:
            if user_bet == turtle.color()[0]:
                print(f'You have won the bet {turtle.color()[0]} turtle is first')
                race_over = False
                break
            else:
                print(f"Sorry you Lose the winner is {turtle.color()[0]} Turtle")
                race_over = False
                break


screen.exitonclick()