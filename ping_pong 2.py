from turtle import Turtle, Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height =600)
screen.title("Ping Pong")
screen.tracer(0)



paddle  = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid = 5,stretch_len = 1)
paddle.penup()
paddle.goto(350,0)

def go_up():
    new_y = paddle.ycor() + 20
    
    paddle.goto(paddle.xcor(),new_y)
    
    
    
    
def go_down(): 
    new_y = paddle.ycor() - 20
    
    paddle.goto(paddle.xcor(),new_y)
    
screen.listen()    
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")

#new paddle:
paddle1  = Turtle()
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid = 5,stretch_len = 1)
paddle1.penup()
paddle1.goto(-350,0)

def go_up():
    new_y = paddle1.ycor() + 20
    
    paddle1.goto(paddle1.xcor(),new_y)
    
    
    
    
def go_down(): 
    new_y = paddle1.ycor() - 20
    
    paddle1.goto(paddle1.xcor(),new_y)
    
screen.listen()    
screen.onkey(go_up,"w")
screen.onkey(go_down,"s")

paddle12  = Turtle()
paddle12.shape("circle")
paddle12.color("white")
paddle12.shapesize(stretch_wid = 0.5,stretch_len = 0.5)
paddle12.penup()
paddle12.goto(0,0)


game_is_on = True
while game_is_on:
    screen.update()





















































screen.exitonclick()




