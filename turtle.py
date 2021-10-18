import turtle

window = turtle.Screen()
screen_height = 500
screen_width = 600
window.setup(screen_width, screen_height)

tree = turtle.Turtle()

#tree.up()
tree.goto(-100, -screen_height/2)
tree.color("brown")
tree.down()
tree.begin_fill()
for i in range(4):
  tree.forward(200)
  tree.left(90)
tree.end_fill()

print(tree.position())

tree.up()
#tree.goto(0, 0)
tree.left(90) #first triangle needs this
tree.forward(200)
tree.right(90)
tree.color("green")
tree.begin_fill()

for i in range(3):
  tree.forward(100*2)
  tree.left(120)

tree.end_fill()

tree.forward(100) #transitioning to 2nd triangle
tree.left(90)#
tree.forward(150) # 200-50
 
tree.right(90)#
tree.backward(50)
tree.begin_fill()#

for i in range(3):#
  tree.forward(100)
  tree.left(120)

tree.end_fill()

tree.forward(50)

tree.left(90)

tree.forward(70)

tree.right(90)
tree.backward(25)
tree.begin_fill()

for i in range(3):
  tree.forward(50)
  tree.left(120)

tree.end_fill()

tree.up()