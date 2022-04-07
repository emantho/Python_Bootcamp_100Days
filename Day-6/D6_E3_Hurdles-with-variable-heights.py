"""
ou should be able to write programs that are valid for worlds Around 4 and Hurdles 3, and ot combine them for this last hurdles race.
Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
"""


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_over():
    turn_right()
    move()
    turn_right()
    move()


while not at_goal():
    if wall_on_right() and not wall_in_front():
        move()
    elif wall_on_right() and wall_in_front():
        turn_left()
    elif not wall_on_right():
        jump_over()
