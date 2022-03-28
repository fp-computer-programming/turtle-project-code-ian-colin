# Author: IBN(AMDG) 3/28/2022

import turtle
import time
import random

name = input("What is your name? ")
window = turtle.Screen()
window.screensize(170, 170)
window.bgcolor("green")
window.title("{0}'s Snake Game".format(name))

head = turtle.Turtle()
head.shape("square")
color = turtle.textinput("Color", "What color should the snake be?")
speed = turtle.textinput("Difficulty", "Enter Easy, Medium, or Hard.")

food = turtle.Turtle()


window.mainloop()