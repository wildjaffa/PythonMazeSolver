from worker import maze
from graphics import time

print('What size maze do you want? (Maximum 70, Minimum 10)')
response = input()
while not response.isdigit() or int(response) > 70 or int(response) < 10:
    print('Invalid number, input a number between 10 and 70')
    response = input()

maze_size = int(response)

mazeWindow = maze(maze_size)

#mazeWindow.move_north()    #moves the user square north
#mazeWindow.move_south()    #moves the user square south
#mazeWindow.move_west()     #moves the user square west
#mazeWindow.move_east()     #moves the user square east
#mazeWindow.get_key_stroke()  #returns Left, Right, Up, or Down
#mazeWindow.has_quit()       #true or false
#mazeWindow.has_won         #true or false
#mazeWindow.can_move_east   #true or false
#mazeWindow.can_move_north  #true or false
#mazeWindow.can_move_south  #true or false
#mazeWindow.can_move_west   #true or false




while not mazeWindow.has_won and not mazeWindow.has_quit():
    key = mazeWindow.get_key_stroke()
    if key == 'Left':
        #TODO: move left
    elif key == 'Right':
        #TODO:  move right
    elif key == 'Up':
        #TODO: move up
    elif key == 'Down':
        #TODO: move down
    elif key == -1:
        break
