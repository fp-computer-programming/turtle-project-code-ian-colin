# Author: IBN(AMDG) 3/28/2022

import turtle
import time
import random

name = input("What is your name? ")
window = turtle.Screen()
window.setup(height=600, width=600)
turtle.colormode(255)
window.bgcolor(105, 224, 49)
window.title("{0}'s Snake Game".format(name))

score = 0
high_score = 0
leaderboard = open("/Users/p22inolan/Desktop/project/turtle-project-code-ian-colin/leaderboard.txt", "a")
with open("/Users/p22inolan/Desktop/project/turtle-project-code-ian-colin/leaderboard.txt") as f:
    first_line = f.readline().strip()
    if first_line == "\n":
        leaderboard.write("INITIALS     SCORE")

head = turtle.Turtle()
head.shape("square")
color = turtle.textinput("Color", "What color should the snake be?")
speed = turtle.textinput("Difficulty", "Enter Easy, Medium, or Hard.")
speed.islower()
if speed == "easy":
    head.speed(1)
if speed == "medium":
    head.speed(2)
if speed == "hard":
    head.speed(3)
head.color(color)
head.penup()
head.goto(0, 0)

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.speed(0)
food.penup()
food.goto(0, 200)

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 270)
scoreboard.write("Score: 0  High Score: 0", align="center", font=("Comic Sans", 24, "bold"))

def snake_up():
    if head.heading != 270:
        head.heading = 90


def snake_down():
    if head.heading != 90:
        head.heading = 270


def snake_left():
    if head.heading != 0:
        head.heading = 180


def snake_right():
    if head.heading != 180:
        head.heading = 0


def movement():
    if head.heading == 90:
        y = head.ycor()
        head.sety(y+20)
    if head.heading == 270:
        y = head.ycor()
        head.sety(y-20)
    if head.heading == 180:
        x = head.xcor()
        head.setx(x-20)
    if head.heading == 0:
        x = head.xcor()
        head.setx(x+20)


window.listen()
window.onkeypress(snake_up, "w")
window.onkeypress(snake_down, "s")
window.onkeypress(snake_left, "a")
window.onkeypress(snake_right, "d")

body = []

#play = window.textinput("Ready?", "Ready to play? (Y/N)")
#play.isupper()

#while play == "Y":
while True:
    window.update()
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        head.color("red")
        time.sleep(1)
        head.penup
        head.goto(0,0)
        for segment in body:
            segment.goto(1000, 1000)
        body.clear()
        scoreboard.clear()
        scoreboard.write("Score: {0}  High Score: {1}".format(score, high_score), align="center", font=("Comic Sans", 24, "bold"))
        initials = window.textinput("Game Over!", "Enter your initials:")
        leaderboard.write("\n {0}         {1}".format(initials, score))
        play_again = window.textinput("Game Over!", "Do you want to play again? (Y/N)")
        play_again.isupper()
        turtle.bye()
    
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
    
        tail = turtle.Turtle()
        tail.speed(0)
        tail.shape("square")
        tail.color(color)
        tail.penup()
        body.append(tail)
        score += 10
        if score > high_score:
            high_score = score
        scoreboard.clear()
        scoreboard.write("Score: {0}  High Score: {1}".format(score, high_score), align="center", font=("Comic Sans", 24, "bold"))

    for index in range(len(body)-1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)
    movement()
    for segment in body:
        if segment.distance(head) < 20:
            head.color("red")
            time.sleep(1)
            head.penup
            head.goto(0,0)
            for segment in body:
                segment.goto(1000, 1000)
            segment.clear()
            scoreboard.clear()
            scoreboard.write("Score: {0}  High Score: {1}".format(score, high_score), align="center", font=("Comic Sans", 24, "bold"))
            initials = window.textinput("Game Over!", "Enter your initials:")
            leaderboard.write("\n {0}         {1}".format(initials, score))
    #play_again = window.textinput("Try Again?", "Do you want to play again? (Y/N)")
    #play_again.isupper

   # if play_again == "N":
    #    turtle.bye()
   # if play == "N":
   #     turtle.bye()
   # elif play != "Y" or "N":
    #    error = window.textinput("Invalid", "Please enter either Y or N. Type OK to continue.")
    #    error.isupper()
    #    if error == "OK":
    #        play

window.mainloop()