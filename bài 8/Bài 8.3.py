print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
import turtle
painter = turtle.Turtle()
painter.pensize(3)
screen = turtle.Screen()
colors = ["red", "green", "blue"]
while True:
    for color in colors:
        painter.pencolor(color) 
        painter.circle(120)      
        painter.setposition(0, 0)  
        painter.right(40)         
screen.mainloop()

