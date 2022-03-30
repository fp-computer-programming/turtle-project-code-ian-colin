# Author: IBN(AMDG) 3/28/2022

import turtle
import time
import random

turtle.colormode(255)
name = input("What is your name? ")
window = turtle.Screen()
window.screensize(500, 500)
window.bgcolor(105, 224, 49)
window.title("{0}'s Snake Game".format(name))

score = 0
high_score = 0

head = turtle.Turtle()
head.shape("square")
color = turtle.textinput("Color", "What color should the snake be?")
speed = turtle.textinput("Difficulty", "Enter Easy, Medium, or Hard.")
speed.islower()
if speed == "easy":
    head.speed(3)
if speed == "medium":
    head.speed(6)
if speed == "hard":
    head.speed(9)
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
        head.sety(y+10)
    if head.heading == 270:
        y = head.ycor()
        head.sety(y-10)
    if head.heading == 180:
        x = head.xcor()
        head.sety(x+10)
    if head.heading == 0:
        x = head.xcor()
        head.sety(x-10)

window.listen()
window.onkeypress(snake_up, "w")
window.onkeypress(snake_down, "s")
window.onkeypress(snake_left, "a")
window.onkeypress(snake_right, "d")

body = []

while True:
    window.update()
    movement()

window.mainloop()