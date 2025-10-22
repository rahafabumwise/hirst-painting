
from turtle import Turtle, Screen,colormode
import random
colormode(255)
# import colorgram

# colors = colorgram.extract("image.jpg",15)

# my_colors = []

# for i in range(15):
#     rgb1 = colors[i].rgb
#     r = rgb1.r
#     g = rgb1.g
#     b = rgb1.b
#     rgb2 = (r , g , b)
    
#     my_colors.append(rgb2)
    

colors_list = [
 (249, 228, 17),
 (213, 13, 9),
 (198, 12, 35),
 (231, 228, 5),
 (197, 69, 20),
 (33, 90, 188),
 (43, 212, 71),
 (234, 148, 40),
 (33, 30, 152),
 (16, 22, 55),
 (66, 9, 49)]


arr = Turtle()
arr.penup()
arr.hideturtle()
arr.setheading(225)
arr.forward(300)
arr.speed("fastest")

for i in range(10):

    for i in range(10):
        random_color = random.choice(colors_list)
        arr.dot(20, random_color)
        arr.setheading(0)
        arr.forward(50)
        
    arr.setheading(90)
    arr.forward(50)
    arr.setheading(180)
    arr.forward(500)










screen = Screen()
screen.exitonclick()