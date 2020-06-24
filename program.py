from worker import maze


mazeWindow = maze(100,100)
while not mazeWindow.has_won:
    key = mazeWindow.get_key_stroke()
    if key == 'Left':
        mazeWindow.move_left()
    elif key == 'Right':
        mazeWindow.move_right()
    elif key == 'Up':
        mazeWindow.move_up()
    elif key == 'Down':
        mazeWindow.move_down()
    elif key == -1:
        break
#time.sleep(1)
#mazeWindow.move_up()
#time.sleep(1)
#mazeWindow.move_up()
#mazeWindow.window.getKey()


