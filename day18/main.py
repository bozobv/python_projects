
import turtle
from colors import random_color
import random


def square(mr_turtle, num=100):
    for _ in range(4):
        mr_turtle.forward(num)
        mr_turtle.left(90)

def dashed(mr_turtle, dash_length=10, gap_length=5, dash_num=10):
    for _ in range(10):
        mr_turtle.forward(dash_length) 
        mr_turtle.penup()  
        mr_turtle.forward(gap_length) 
        mr_turtle.pendown()  

def draw_shape(mr_turtle, sides_num, side_length=100):
    
    turning_angle = 360 / sides_num
    
    for _ in range(sides_num):
        mr_turtle.forward(side_length)
        mr_turtle.left(turning_angle)

def turn_random(mr_turtle, directions=4, turn_angle=90):
    mr_turtle.left(random.randint(0,directions-1)*90)

def random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255)) 

def random_walk(mr_turtle, walk_iterations=100, walk_len=30, pen_width=15):
    mr_turtle.speed(0)
    mr_turtle.width(pen_width)
    for _ in range(walk_iterations):
        turn_random(mr_turtle=mr_turtle)
        mr_turtle.pencolor(random_color() )
        mr_turtle.forward(walk_len)

def funny_circles(mr_turtle, circle_num=20, circle_radius=100):
    mr_turtle.speed(0)

    for _ in range(circle_num):
        mr_turtle.pencolor(random_color() )
        mr_turtle.circle(radius=circle_radius)
        mr_turtle.left(360/circle_num)

def art_new_line(mr_turtle,dot_num_width,dot_space):
    mr_turtle.penup()      
    mr_turtle.right(180)
    mr_turtle.forward(dot_num_width*dot_space)
    mr_turtle.right(90)
    mr_turtle.forward(dot_space)
    mr_turtle.right(90)

def create_art(mr_turtle, dot_num_height=10, dot_num_width=10, dot_size=20, dot_space=50):
    
    mr_turtle.penup()  
    mr_turtle.right(90)
    mr_turtle.forward(dot_num_height/2 *((dot_size+dot_space)-dot_size/2))
    mr_turtle.right(90)
    mr_turtle.forward(dot_num_height/2 *((dot_size+dot_space)-dot_size/2))
    mr_turtle.right(180)

    for _ in range(dot_num_height):
        for _ in range(dot_num_width):
            mr_turtle.pencolor(random_color() )
            mr_turtle.penup()  
            mr_turtle.forward(dot_space)
            mr_turtle.pendown()  

            mr_turtle.dot(dot_size)
        art_new_line(mr_turtle,dot_num_width,dot_space)


screen = turtle.Screen()
#screen.bgcolor("black")
turtle.colormode(255)


sanyi = turtle.Turtle()
sanyi.shape("turtle")
sanyi.color("coral" , "green")

#square(sanyi)
#sanyi.right(90)
#dashed(sanyi)

#draw_shape(sanyi, 12)
#draw_shape(sanyi, 8)
#draw_shape(sanyi, 5)

#random_walk(sanyi)
#funny_circles(sanyi,500,200)
create_art(sanyi)

screen.exitonclick()