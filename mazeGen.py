import random

class maze_builder:

    def __flip_bit(self, row, num):
        ret = row[0 : num] + '0' + row[num + 1 : len(row)]
        return ret

    def __check_down(self, x_pos, y_pos):
        if y_pos == self.__max_y:
            return False
        potential_y = y_pos + 1
        if(potential_y == self.__max_y and x_pos == self.__mid_x):
            return True
        if self.string_list[potential_y][x_pos] == '0':
            return False
        if x_pos != 0 and self.string_list[potential_y][x_pos - 1] == '0':
            return False
        if x_pos != self.__max_x and self.string_list[potential_y][x_pos + 1] == '0':
            return False
        return True

    def __check_up(self, x_pos, y_pos):
        if y_pos == 0:
            return False
        potential_y = y_pos - 1
        if self.string_list[potential_y][x_pos] == '0':
            return False
        if x_pos != 0 and self.string_list[potential_y][x_pos - 1] == '0':
            return False
        if x_pos != self.__max_x and self.string_list[potential_y][x_pos + 1] == '0':
            return False
        return True

    def __check_right(self, x_pos, y_pos):
        if x_pos == self.__max_x:
            return False
        potential_x = x_pos + 1
        if(potential_x == self.__mid_x and y_pos == self.__max_y):
            return True
        if self.string_list[y_pos][potential_x] == '0':
            return False
        if y_pos != 0 and self.string_list[y_pos - 1][potential_x] == '0':
            return False
        if y_pos != self.__max_y and self.string_list[y_pos + 1][potential_x] == '0':
            return False
        return True

    def __check_left(self, x_pos, y_pos):
        if x_pos == 0:
            return False
        potential_x = x_pos - 1
        if(potential_x == self.__mid_x and y_pos == self.__max_y):
            return True
        if self.string_list[y_pos][potential_x] == '0':
            return False
        if y_pos != 0 and self.string_list[y_pos - 1][potential_x] == '0':
            return False
        if y_pos != self.__max_y and self.string_list[y_pos + 1][potential_x] == '0':
            return False
        return True


    def generate_maze(self, fileName, height, width):
        self.height = height
        self.width = width
        self.__max_y = height - 1
        self.__max_x = width - 1
        self.__mid_x = width // 2
        self.string_list = list()
        #while True:
        row = ''
        for i in range(self.width):
            row += '1'
        for i in range(self.height):
            self.string_list.append(row)
        #string_list[0][5] = '0'
        self.string_list[0] = self.__flip_bit(self.string_list[0], self.width // 2)
        self.__generate_path(self.__mid_x, 0, 'up')
        #    if self.string_list[height - 1][self.width // 2] == '0':
        #        break
        full_maze = ''
        for row in self.string_list:
            full_maze += row + '\n'
        with open(fileName, 'w') as file:
            file.write(full_maze)

    def __generate_path(self, x_pos, y_pos, previous):
        right_tried = previous == 'right'
        left_tried = previous == 'left'
        up_tried = previous == 'up'
        down_tried = previous == 'down'
        self.string_list[y_pos] = self.__flip_bit(self.string_list[y_pos], x_pos)
        while(right_tried + left_tried + up_tried + down_tried < 3):
            try_path = random.choice([1,2,3,4])
            if try_path == 1 and not right_tried :
                if self.__check_right(x_pos, y_pos):
                    self.__generate_path(x_pos + 1, y_pos, 'left')
                right_tried = True
            elif try_path == 2 and not left_tried:
                if self.__check_left(x_pos, y_pos):
                    self.__generate_path(x_pos - 1, y_pos, 'right')
                left_tried = True
            elif try_path == 3 and not up_tried:
                if self.__check_up(x_pos, y_pos):
                    self.__generate_path(x_pos, y_pos - 1, 'down')
                up_tried = True
            elif try_path == 4 and not down_tried:
                if self.__check_down(x_pos, y_pos):
                    self.__generate_path(x_pos, y_pos + 1, 'up')
                down_tried = True
        return
    


    

#generate_maze('')
