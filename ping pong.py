from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from news_score_board import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height =600)
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
  
score = Scoreboard()  
screen.listen()    
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Detect collision with wall
    if ball.ycor() >280 or ball.ycor()< -280:
        #+300 means that of the top wall and the lower -300 for the lower walls
        ball.bounce_y()
        
        
    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320:
        ball.bounce_x()
    if ball.distance(l_paddle) < 40 and ball.xcor() >-340:
        ball.bounce_x()
        
        
    #missing of the ball from the right paddle:
    if ball.xcor() <-380:
        ball.reset()
        score.l_point()
        
    #missing of the left paddle
    if ball.xcor() >380:
        ball.reset()
        score.r_point
        
        
        
        
        
        
screen.exitonclick()




