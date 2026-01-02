import turtle
import random
from idlelib.multicall import MC_ENTER

#screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Catch the Turtle")
screen.bgcolor("lightblue")

#turtle
t=turtle.Turtle()
t.shape("turtle")
t.color("darkgreen")
t.shapesize(1.5,1.5)
t.penup()
t.speed(0)

#score
score_writer=turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-280,260)

#timer
time_writer=turtle.Turtle()
time_writer.hideturtle()
time_writer.penup()
time_writer.goto(220,260)

#variables
score = 0
miss=0
game_time=30
turtle_visible=False
time_limit = 3000

def update_score():
    score_writer.clear()
    score_writer.write(f"Score: {score} Miss:  {miss}", font=("Arial", 12, "bold"))

def update_time():
    time_writer.clear()
    time_writer.write(f"Time: {game_time}", font=("Arial", 12, "bold"))

def move_turtle():
    global turtle_visible, miss

    if turtle_visible:
        miss+=1

    t.hideturtle()
    x=random.randint(-250,250)
    y=random.randint(-250,250)
    t.goto(x,y)
    t.showturtle()
    turtle_visible=True

    update_score()
    screen.ontimer(move_turtle,time_limit)

#click the mouse
def catch(x,y):
    global score,turtle_visible
    if turtle_visible:
        score+=1
        turtle_visible=False
        t.hideturtle()
        update_score()

def countdown():
    global game_time
    if game_time>0:
        game_time-=1
        update_time()
        screen.ontimer(countdown,1000)
    else:
        end_game()

def end_game():
    t.hideturtle()
    score_writer.goto(0,0)
    score_writer.write(
        f"GAME OVER\nScore: {score}\nMiss: {miss}",
        align=center,
        font=("Arial", 16, "bold"))

t.onclick(catch)

update_score()
update_time()
move_turtle()
countdown()

screen.mainloop()