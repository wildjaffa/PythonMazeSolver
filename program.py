from graphics import *
win = GraphWin(width = 500, height = 500) # create a window
win.setCoords(0, 0, 100, 100) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)

mySquare = Rectangle(Point(1, 1), Point(9, 9)) # create a rectangle from (1, 1) to (9, 9)
mySquare.draw(win) # draw it to the window
win.getMouse() # pause before closing