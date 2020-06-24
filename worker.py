from graphics import *


class maze:


    def __init__(self, maze_height, maze_width):
        self.__window = GraphWin(width = 500, height = 500) # create a window
        self.__window.setCoords(0, 0, maze_width, maze_height) # set the coordinates of the window; bottom left is (0, 0) and top right is (100, 100)


        background = Rectangle(Point(0,0),Point(100,100))
        background.setFill('gray')
        background.draw(self.__window)

        self.__string_list = list()
        self.__squares = list()

        y_axis = 100
        with open('Maze.txt', 'r') as maze_text:
            for row in maze_text:
                x_axis = 0
                row_squares = list()
                for i in range(len(row)):
                    current = row[i]
                    if current == '1':
                        my_square = Rectangle(Point(x_axis, y_axis - 10), Point(x_axis + 10, y_axis))
                        my_square.setFill('black')
                        my_square.draw(self.__window)
                        row_squares.append(my_square)
                    elif current == '0':
                        my_square = Rectangle(Point(x_axis, y_axis - 10), Point(x_axis + 10, y_axis))
                        my_square.setFill('gray')
                        my_square.setOutline('gray')
                        my_square.draw(self.__window)
                        row_squares.append(my_square)
                    x_axis += 10
                self.__squares.append(row_squares)
                y_axis -= 10
                self.__string_list.append(row)
        
        self.player_x = 5
        self.player_y = 0
        self.has_won = False
        self.__check_movement_ability()
        self.player = Rectangle(Point(self.player_x*10, self.player_y*10), Point((self.player_x + 1)*10, (self.player_y + 1)*10))
        self.player.setFill('red')
        self.player.draw(self.__window)


    def __check_movement_ability(self):
        current_row = self.__string_list[9 - self.player_y]
        self.can_move_left = self.player_x > 0 and current_row[self.player_x - 1] == '0'
        self.can_move_right = self.player_x < 9 and current_row[self.player_x + 1] == '0'
        self.can_move_up = self.player_y < 9 and self.__string_list[9 - self.player_y - 1][self.player_x] == '0'
        self.can_move_down = self.player_y > 0 and self.__string_list[9 - self.player_y + 1][self.player_x] == '0'
        self.has_won = self.player_x == 5 and self.player_y == 9

    def move_up(self):
        if self.can_move_up:
            self.__move_player(0,1)
    
    def move_down(self):
        if self.can_move_down:
            self.__move_player(0, -1)
    
    def move_left(self):
        if self.can_move_left:
            self.__move_player(-1, 0)

    def move_right(self):
        if self.can_move_right:
            self.__move_player(1, 0)

    def get_key_stroke(self):
        return self.__window.getKey()

    def __move_player(self, x, y):
        prev_square = self.__squares[9 - self.player_y][self.player_x]
        if prev_square.config['outline'] == 'gray':
            prev_square.setFill('green')
            prev_square.setOutline('green')
        else:
            prev_square.setFill('purple')
            prev_square.setOutline('purple')
        #back_square.draw(self.__window)

        #self.player.draw(self.__window)
        for i in range(0,10):
            self.player.move(x, y)
            time.sleep(.01)
        self.player_x += x
        self.player_y += y
        self.__check_movement_ability()




