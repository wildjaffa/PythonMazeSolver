from worker import maze
from graphics import time

print('What size maze do you want? (Maximum 70, Minimum 10)')
response = input()
while not response.isdigit() or int(response) > 70 or int(response) < 10:
    print('Invalid number, input a number between 10 and 70')
    response = input()

maze_size = int(response)

print('Auto Solve? (y/n)')
response = input()
while not response.lower() == 'y' and not response.lower() == 'n':
    print('Unrecognized response, input y or n')
    response = input()

mazeWindow = maze(maze_size)

if response == 'n:':
    while not mazeWindow.has_won and not mazeWindow.has_quit():
        key = mazeWindow.get_key_stroke()
        if key == 'Left':
            mazeWindow.move_west()
        elif key == 'Right':
            mazeWindow.move_east()
        elif key == 'Up':
            mazeWindow.move_north()
        elif key == 'Down':
            mazeWindow.move_south()
        elif key == -1:
            break
else:
    previous_move = 'north'
    while not mazeWindow.has_won and not mazeWindow.has_quit():
        if previous_move == 'north':
            if mazeWindow.can_move_east:
                mazeWindow.move_east()
                previous_move = 'east'
            elif mazeWindow.can_move_north:
                mazeWindow.move_north()
                previous_move = 'north'
            elif mazeWindow.can_move_west:
                mazeWindow.move_west()
                previous_move = 'west'
            else:
                mazeWindow.move_south()
                previous_move = 'south'
        elif previous_move == 'east':
            if mazeWindow.can_move_south:
                mazeWindow.move_south()
                previous_move = 'south'
            elif mazeWindow.can_move_east:
                mazeWindow.move_east()
                previous_move = 'east'
            elif mazeWindow.can_move_north:
                mazeWindow.move_north()
                previous_move = 'north'
            else:
                mazeWindow.move_west()
                previous_move = 'west'
        elif previous_move == 'south':
            if mazeWindow.can_move_west:
                mazeWindow.move_west()
                previous_move = 'west'
            elif mazeWindow.can_move_south:
                mazeWindow.move_south()
                previous_move = 'south'
            elif mazeWindow.can_move_east:
                mazeWindow.move_east()
                previous_move = 'east'
            else:
                mazeWindow.move_north()
                previous_move = 'north'
        else:
            if mazeWindow.can_move_north:
                mazeWindow.move_north()
                previous_move = 'north'
            elif mazeWindow.can_move_west:
                mazeWindow.move_west()
                previous_move = 'west'
            elif mazeWindow.can_move_south:
                mazeWindow.move_south()
                previous_move = 'south'
            else:
                mazeWindow.move_east()
                previous_move = 'east'
        #time.sleep(.25)

        

#time.sleep(1)
#mazeWindow.move_up()
#time.sleep(1)
#mazeWindow.move_up()
#mazeWindow.window.getKey()

