# [Coding Exercise] Week 6 - My signed turtle work of art
# Author: Jasper Song
# Date: Oct 17 2021

import turtle
import random

window = turtle.Screen()
tree = turtle.Turtle()
screen_height = 500
screen_width = 600
window.setup(screen_width, screen_height)

def draw_triangle(size):
  pass

def draw_trunk():
  tree.goto(-100, -screen_height/2)
  tree.color("brown")
  tree.down()
  tree.begin_fill()
  for i in range(4):
    tree.forward(200)
    tree.left(90)
  tree.end_fill()

def draw_tree():
  tree.up()
  tree.color("green")

  draw_triangle()

  tree.begin_fill()

  for i in range(3):
    tree.forward(100*size)
    tree.left(120)

  tree.end_fill()
draw_tree(2, screen_width/2, screen_height)
# This line has exactly 100 characters (including the period), use it to keep each line under limit.
bauble_colours = ["yellow", "blue", "red", "silver"]
def draw_bauble(amount):
  for i in range(amount):
    tree.up()
    tree.left(200)
    tree.backward(50)
    tree.shape("circle")
    tree.color(random.choice(bauble_colours))
    tree.stamp()

def draw_garland():
  tree.color("red")


  

draw_bauble(6)





draw_trunk()