# Hurdle challenge using while loop.
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
# Output: Robot jumps over hurdles and reaches the goal.
# The code is more readable and concise than using a for loop.
# The while loop is more flexible and powerful than the for loop.
# The while loop can be used to solve a wide variety of problems.
# The for loop is more limited in its application.
# The while loop is more versatile and can be used in more situations.
# The for loop is more specialized and is best suited for iterating over a sequence of items.
# The while loop is more general and can be used for a wider range of tasks.
# The for loop is more efficient for iterating over a sequence of items.
# The while loop is more flexible and can be used in more complex situations.
# The for loop is more limited in its application and is best suited for simple iteration tasks.
# The while loop is more powerful and can be used to solve a wide variety of problems.
# The for loop is more specialized and is best suited for iterating over a sequence of items.
# The while loop is more versatile and can be used in more situations.  
# The for loop is more limited in its application.
# The while loop is more general and can be used for a wider range of tasks.
# The for loop is more efficient for iterating over a sequence of items.
# The while loop is more flexible and can be used in more complex situations.
# The for loop is more limited in its application and is best suited for simple iteration tasks.
