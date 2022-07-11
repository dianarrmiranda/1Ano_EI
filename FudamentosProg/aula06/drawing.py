#Exercício 02 ficha 06
import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
with open('drawing.txt') as file:
    for line in file:
        if line == "UP\n":
            t.up()
        elif line == "DOWN\n":
            t.down()
        else:
            t.goto(int(line.split()[0]), int(line.split()[1]))

# wait
turtle.Screen().exitonclick()

