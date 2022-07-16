import turtle

# Screen Dimensions and Delay (ms)
WIDTH, HEIGHT, DELAY = 600, 600, 100

# Initial Snake on x-axis and it's direction
snake = [[0,0], [20,0], [40,0], [60,0], [80,0]]





snake_direction = "up"
offsets = {
    "up": (0,20),
    "down": (0,-20),
    "left": (-20,0),
    "right": (20,0)
}

def go_up():
    # To change snake direction
    global snake_direction
    '''Snake can only do 90 degree turns
        if it's heading down it can't go up 
        since that would mean its moving over itself. 
    '''
    if snake_direction != 'down':
        snake_direction = 'up'

def go_right():
    global snake_direction
    if snake_direction != 'left':
        snake_direction = 'right'

def go_down():
    global snake_direction
    if snake_direction != 'up':
        snake_direction = 'down'

def go_left():
    global snake_direction
    if snake_direction != 'right':
        snake_direction = 'left'

def move_snake():

    # Increment Head location and Pop tail location to maintain Snake Size
    my_turtle.clearstamps()
    new_head = snake[-1].copy()
    
    # X[0] and Y[1] location updates from offset Dictionary containing direction 

    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    snake.append(new_head)
    snake.pop(0)
    
    for location in snake:
        my_turtle.goto(location[0], location[1])
        my_turtle.stamp()

    canvas.update()
    turtle.ontimer(move_snake, DELAY)


###Canvas
canvas = turtle.Screen()
canvas.setup(WIDTH, HEIGHT)
canvas.title("Snake")
canvas.bgcolor('Black')
canvas.tracer(0)
#####



# Event Handler
canvas.listen()
canvas.onkey(go_up, "Up")
canvas.onkey(go_right, "Right")
canvas.onkey(go_down, "Down")
canvas.onkey(go_left, "Left")


# ////Turtle Object Description
my_turtle = turtle.Turtle()
my_turtle.shape("square")
my_turtle.color("white", "red")
my_turtle.penup()
my_turtle.stamp()



# Move Snake Along X-Axis
move_snake()


# Infinite loop to keep canvas open until 
# user presses X
turtle.done()