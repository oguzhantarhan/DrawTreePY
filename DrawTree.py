from turtle import Turtle, Screen
wn = Screen()
turtle = Turtle()
print("input size")
size = int(input())
print("input level")
level = int(input())
def tree(turtle,level,size):
    if(level!=0):
        turtle.forward(size)
        turtle.right(60)
        tree(turtle,level-1,2*size/3)
        turtle.left(120)
        tree(turtle,level-1,2*size/3)
        turtle.right(60)
        turtle.backward(size)
turtle.left(90)
tree(turtle,level,size)
wn.exitonclick()
