from worker import maze
from graphics import time

print('What size maze do you want? (Maximum 70, Minimum 10)')
response = input()
while not response.isdigit() or int(response) > 70 or int(response) < 10:
    print('Invalid number, input a number between 10 and 70')
    response = input()

maze_size = int(response)

mazeWindow = maze(maze_size)
#mazeWindow.move_north() 
#mazeWindow.move_south() 
#mazeWindow.move_west()
#mazeWindow.move_east()

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
