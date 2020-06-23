from graphics import *
win = GraphWin(width = 500, height = 500) # create a window
win.setCoords(0, 0, 100, 100) # set the coordinates of the window; bottom left is (0, 0) and top right is (100, 100)


background = Rectangle(Point(0,0),Point(100,100))
background.setFill('white')
background.draw(win)
#mySquare = Rectangle(Point(0, 0), Point(9, 9)) # create a rectangle from (1, 1) to (9, 9)
#mySquare.setFill('red')
#mySquare.draw(win) # draw it to the window
#mySquare = Rectangle(Point(0,0), Point(19,19))
#mySquare.draw(win)
#mySquare = Line(Point(10,20), Point(30,30))
#mySquare.draw(win)
#mySquare = Rectangle(Point(90, 90), Point(100,100))
#mySquare.draw(win)
corner = 10
#myLine = Line(Point(0,0), Point(100,100))
#myLine.draw(win)

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
                #my_line = Line(Point(x_axis, y_axis), Point(x_axis, y_axis-10))
                #my_line.draw(win)
                #my_line = Line(Point(x_axis + 10, y_axis), Point(x_axis + 10, y_axis - 10))
                #my_line.draw(win)
            
            x_axis += 10
        previous = row
        y_axis -= 10

#print(f.read())
#while(f.readline)

#myLine = Line(Point(0, 100), Point(100, 0))
#myLine.draw(win)
#for i in range(0,10):
    #mySquare = Rectangle(Point(corner, corner), Point(corner + 10, corner + 10))
    #mySquare.draw(win)
#    myLine = Line(Point(10, corner),Point(10, corner + 10))
#    myLine.draw(win)
#    corner += 10



try:
    win.getMouse() # pause before closing
except:
    print('Done')