from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        
    
    #Detect collision with paddle
    def bounce_y(self):
        #this is used to change the direction of the ball when it collide with the wall or with the paddle
        #in this case the vertical axis or number are changing not the horizontal number12
        self.y_move *= -1
        
        
    #Detect collsion in the opposite direction of the axis
    def bounce_x(self):
        self.x_move *=-1
        self.move_speed *= 0.9
    
    #this is use to restart the game when the ball has been missed up
    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()