UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
DOWN_ARROW = 'Down'
RIGHT_ARROW = 'Right'
SPACEBAR = 'space'

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

direction = UP

def up():
    global direction    
    direction = UP
    print("You dun pressed the Up key")

    onekeypress(function_name, key)

    turtle.onkeypress(up, UP_ARROW)
    turtle.onkeypress(down, DOWN_ARROW)
    turtle.onkeypress(left, LEFT_ARROW)
    turtle.onkeypress(right, RIGHT_ARROW)

    turtle.listen()
    
