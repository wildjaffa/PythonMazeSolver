from graphics import Rectangle, Point, GraphWin, time
from mazeGen import maze_builder


class maze:


    def move_north(self):
        if self.can_move_north:
            self.__move_player(0,1)
    
    def move_south(self):
        if self.can_move_south:
            self.__move_player(0, -1)
    
    def move_west(self):
        if self.can_move_west:
            self.__move_player(-1, 0)

    def move_east(self):
        if self.can_move_east:
            self.__move_player(1, 0)

    def __init__(self, size, file_name = ''):
        self.__window = GraphWin(width = 500, height = 500) # create a window
        self.__window.setCoords(0, 0, size * 10, size * 10) # set the coordinates of the window; bottom left is (0, 0) and top right is (100, 100)

        background = Rectangle(Point(0,0),Point(size * 10, size * 10))
        background.setFill('gray')
        background.draw(self.__window)

        self.__string_list = list()
        self.__squares = list()
        self.maze_height = size - 1 #the height is only used as height, so it's easier to make it zero indexed here
        self.maze_width = size #the width is used to calculate the middle, as such it's important we keep the original number
        #and just subtract as needed
        if file_name == '':
            builder = maze_builder()
            builder.generate_maze('Maze3.txt', size, size)
            file_name = 'Maze3.txt'
        with open(file_name, 'r') as maze_text:
            y_axis = size * 10
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
        
        #draw the win square
        win_x = (self.maze_width // 2) * 10
        win_y = self.maze_height * 10
        win_square = Rectangle(Point(win_x, win_y),Point(win_x + 10, win_y + 10))
        win_square.setFill('blue')
        win_square.setOutline('blue')
        win_square.draw(self.__window)

        #draw the player
        for i in range(len(self.__string_list[self.maze_height])):
            if self.__string_list[self.maze_height][i] == '0':
                self.player_x = i
                break
        self.player_y = 0
        self.has_won = False
        self.__check_movement_ability()
        self.player = Rectangle(Point(self.player_x*10, self.player_y*10), Point((self.player_x + 1)*10, (self.player_y + 1)*10))
        self.player.setFill('red')
        self.player.draw(self.__window)       


    def __check_movement_ability(self):
        current_row = self.__string_list[self.maze_height - self.player_y]
        self.can_move_west = bool(self.player_x > 0 and current_row[self.player_x - 1] == '0')
        self.can_move_east = bool(self.player_x < self.maze_width - 1 and current_row[self.player_x + 1] == '0')
        self.can_move_north = bool(self.player_y < self.maze_height and self.__string_list[self.maze_height - self.player_y - 1][self.player_x] == '0')
        self.can_move_south = bool(self.player_y > 0 and self.__string_list[self.maze_height - self.player_y + 1][self.player_x] == '0')
        self.has_won = self.player_x == self.maze_width // 2 and self.player_y == self.maze_height

    def get_key_stroke(self):
        return self.__window.getKey()

    def has_quit(self):
        return self.__window.isClosed()

    def __move_player(self, x, y):
        prev_square = self.__squares[self.maze_height - self.player_y][self.player_x]
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




