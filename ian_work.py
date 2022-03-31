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

score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 325)
score.write("Score: 0  High Score: 0", align="center", font=("Comic Sans", 24, "bold"))

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

while True:
    window.update()
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        head.color("red")
        time.sleep(1)
        head.penup
        head.goto(0,0)
        initials = window.textinput("Game Over!", "Enter your initials:")
        leaderboard.write("\n {0}         {1}".format(initials, score))
        turtle.bye()
    for segment in segments:
        segment.goto(1000, 1000)
    
    movement()

window.mainloop()