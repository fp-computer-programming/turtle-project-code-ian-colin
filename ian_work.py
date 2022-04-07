# Author: IBN(AMDG) 3/28/2022

import turtle
import time
import random

# name input & setting up main window
name = input("What is your name? ")
window = turtle.Screen()
window.setup(height=600, width=600)
turtle.colormode(255)
window.bgcolor(105, 224, 49)
window.title("{0}'s Snake Game".format(name))

# setting score & leaderboard writing
score = 0
high_score = 0
leaderboard = open("leaderboard.txt", "a")
with open("leaderboard.txt") as f:
    first_line = f.readline().strip()
    if first_line == "":
        leaderboard.write("INITIALS     SCORE")

# creating snake head turtle & placing it at start
head = turtle.Turtle()
head.shape("square")
color = turtle.textinput("Color", "What color should the snake be?")
speed = turtle.textinput("Difficulty", "Enter Easy, Medium, or Hard.")
shape = turtle.textinput("Shape", "What shape should the snake be?")
speed.islower()
if speed == "easy":
    head.speed(1)
if speed == "medium":
    head.speed(2)
if speed == "hard":
    head.speed(3)
head.color(color)
head.shape(shape)
head.penup()
head.goto(0, 0)

# creating food and placing it in starting position
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.speed(0)
food.penup()
food.goto(0, 200)

# writing scoreboard turtle
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 270)
scoreboard.write("Score: 0  High Score: 0", align="center", font=("Comic Sans", 24, "bold"))


# direction functions
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


# movement function
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


# binding movements to keys
window.listen()
window.onkeypress(snake_up, "w")
window.onkeypress(snake_down, "s")
window.onkeypress(snake_left, "a")
window.onkeypress(snake_right, "d")

body = []  # list for tail appending

while True:
    window.update()
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:  # if statment for collisions with wall
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
        leaderboard.write("\n{0}         {1}".format(initials, score))

        play_again = window.textinput("Game Over!", "Do you want to play again? (Y/N)")  # play again inputs w/ error message for invalid
        play_again.isupper()
        if play_again == "N":
            turtle.bye()
        if play_again == "Y":
            turtle.bye()
            print("Please relaunch the game to play again.")
        else:
            error = window.textinput("Invalid Input", "Please enter either Y or N. Type OK to continue.")
            error.isupper()
            if error == "OK":
                play_again = window.textinput("Game Over!", "Do you want to play again? (Y/N)")
                play_again.isupper()
                if play_again == "N":
                    turtle.bye()
                elif play_again == "Y":
                    turtle.bye()
            else:
                turtle.bye()
                print("You're really bad at following instructions.")

    if head.distance(food) < 20:  # if statement for randomizing food placement after eating
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        tail = turtle.Turtle()  # tail turtle setup & appending to body list
        tail.speed(0)
        tail.shape("square")
        tail.color(color)
        tail.penup()
        body.append(tail)
        score += 10  # increase in score w/ each new tail segment
        if score > high_score:
            high_score = score
        scoreboard.clear()
        scoreboard.write("Score: {0}  High Score: {1}".format(score, high_score), align="center", font=("Comic Sans", 24, "bold"))

    for index in range(len(body)-1, 0, -1):  # for loop for tail movements
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)

    if len(body) > 0:  # resetting body
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

    movement()

    for segment in body:
        if segment.distance(head) < 20:  # if statment for collisions with tail
            head.color("red")
            time.sleep(1)
            head.penup
            head.goto(0, 0)
            for segment in body:
                segment.goto(1000, 1000)
            segment.clear()
            scoreboard.clear()
            scoreboard.write("Score: {0}  High Score: {1}".format(score, high_score), align="center", font=("Comic Sans", 24, "bold"))
            initials = window.textinput("Game Over!", "Enter your initials:")
            leaderboard.write("\n{0}         {1}".format(initials, score))

            play_again = window.textinput("Game Over!", "Do you want to play again? (Y/N)")
            play_again.isupper()
            if play_again == "N":
                turtle.bye()
            elif play_again == "Y":
                turtle.bye()
                print("Please relaunch the game to play again.")
            else:
                error = window.textinput("Invalid Input", "Please enter either Y or N. Type OK to continue.")
                error.isupper()
                if error == "OK":
                    play_again = window.textinput("Game Over!", "Do you want to play again? (Y/N)")
                    play_again.isupper()
                    if play_again == "N":
                        turtle.bye()
                    elif play_again == "Y":
                        turtle.bye()
                else:
                    turtle.bye()
                    print("You're really bad at following instructions.")


window.mainloop()
