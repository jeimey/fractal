import turtle

window = turtle.Screen()
window.bgcolor("black")
dave = turtle.Turtle()
#dave.shape("turtle")
dave.color("yellow")
dave.speed(0)
dave.pensize(1)

def draw_triangle(turtle_name, size):
    for x in range(1,4):
        turtle_name.right(120)
        turtle_name.forward(size)

def draw_fractal(turtle_name, length=600,recursion=0,origin=1):
    if recursion == 0:
        turtle_name.penup()
        turtle_name.setpos(300,300)
        turtle_name.pendown()
    recursion= recursion + 1
    


 
    if recursion < 5:
            draw_triangle(dave,length)
            turtle_name.right(120)
            turtle_name.forward(length/2)
            turtle_name.left(60)
            length = length / 2
            draw_fractal(turtle_name,length,origin,recursion)
    else:        
        turtle_name.hideturtle()        

                
        


        
            
    window.exitonclick()

draw_fractal(dave) 
