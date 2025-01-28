import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
octagon = turtle.Turtle()

num_sides = 1
side_length = 15
angle = 360/num_sides
for i in range(num_sides):
    octagon.forward(side_length)
    octagon.right(angle)
turtle.done()

    
    

