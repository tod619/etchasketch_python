from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!",
                            prompt="Which turtle will win the race? Pick a colour: ")
print(user_bet)
screen.exitonclick()
