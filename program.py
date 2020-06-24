from graphics import *

#def move_up(current_x, current_y, my_square):
#    for i in range(0,10):
#        my_square.move(current_x*10, current_y*10 + i)
#        time.sleep(.1)

win = GraphWin(width = 500, height = 500) # create a window
win.setCoords(0, 0, 100, 100) # set the coordinates of the window; bottom left is (0, 0) and top right is (100, 100)


background = Rectangle(Point(0,0),Point(100,100))
background.setFill('gray')
background.draw(win)

string_list = list()

previous = ''
y_axis = 100
with open('Maze.txt', 'r') as maze_text:
    for row in maze_text:
        x_axis = 0
        for i in range(len(row)):
            current = row[i]
            if current == '1':
                my_square = Rectangle(Point(x_axis, y_axis - 10), Point(x_axis + 10, y_axis))
                my_square.setFill('black')
                my_square.draw(win)
            
            x_axis += 10
        previous = row
        y_axis -= 10
        string_list.append(row)
current_x = 5
current_y = 0 
my_square = Rectangle(Point(current_x*10, current_y*10), Point((current_x + 1)*10, (current_y + 1)*10))
my_square.setFill('red')
my_square.draw(win)
time.sleep(1)
#my_square.move(0, 10)
#move_up(current_x, current_y, my_square)
for i in range(0,10):
    my_square.move(0, 1)
    time.sleep(.01)

try:
    win.getMouse() # pause before closing
except:
    print('Done')


