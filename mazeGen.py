import random

class maze_builder:
    def __init__(self, height, width):
        self.height = height
        self.width = width

def flip_bit(row, num):
    ret = row[0 : num] + '0' + row[num + 1 : len(row)]
    return ret

def check_down(string_list, x_pos, y_pos):
    if y_pos == 9:
        return False
    potential_y = y_pos + 1
    if(potential_y == 9 and x_pos == 5):
        return True
    if string_list[potential_y][x_pos] == '0':
        return False
    if x_pos != 0 and string_list[potential_y][x_pos - 1] == '0':
        return False
    if x_pos != 9 and string_list[potential_y][x_pos + 1] == '0':
        return False
    return True

def check_up(string_list, x_pos, y_pos):
    if y_pos == 0:
        return False
    potential_y = y_pos - 1
    if string_list[potential_y][x_pos] == '0':
        return False
    if x_pos != 0 and string_list[potential_y][x_pos - 1] == '0':
        return False
    if x_pos != 9 and string_list[potential_y][x_pos + 1] == '0':
        return False
    return True

def check_right(string_list, x_pos, y_pos):
    if x_pos == 9:
        return False
    potential_x = x_pos + 1
    if(potential_x == 5 and y_pos == 9):
        return True
    if string_list[y_pos][potential_x] == '0':
        return False
    if y_pos != 0 and string_list[y_pos - 1][potential_x] == '0':
        return False
    if y_pos != 9 and string_list[y_pos + 1][potential_x] == '0':
        return False
    return True

def check_left(string_list, x_pos, y_pos):
    if x_pos == 0:
        return False
    potential_x = x_pos - 1
    if(potential_x == 5 and y_pos == 9):
        return True
    if string_list[y_pos][potential_x] == '0':
        return False
    if y_pos != 0 and string_list[y_pos - 1][potential_x] == '0':
        return False
    if y_pos != 9 and string_list[y_pos + 1][potential_x] == '0':
        return False
    return True


def generate_maze(fileName, height, width):
    string_list = list()
    row = ''
    for i in range(width):
        row += '1'
    for i in range(height):
        string_list.append(row)
    #string_list[0][5] = '0'
    string_list[0] = flip_bit(string_list[0], width // 2)
    generate_path(string_list, 5, 0, 'up')
    full_maze = ''
    for row in string_list:
        full_maze += row + '\n'
    with open(fileName, 'w') as file:
        file.write(full_maze)

def generate_path(string_list, x_pos, y_pos, previous):
    right_tried = previous == 'right'
    left_tried = previous == 'left'
    up_tried = previous == 'up'
    down_tried = previous == 'down'
    string_list[y_pos] = flip_bit(string_list[y_pos], x_pos)
    while(right_tried + left_tried + up_tried + down_tried < 3):
        try_path = random.choice([1,2,3,4])
        if try_path == 1 and not right_tried :
            if check_right(string_list, x_pos, y_pos):
                generate_path(string_list, x_pos + 1, y_pos, 'left')
            right_tried = True
        elif try_path == 2 and not left_tried:
            if check_left(string_list, x_pos, y_pos):
                generate_path(string_list, x_pos - 1, y_pos, 'right')
            left_tried = True
        elif try_path == 3 and not up_tried:
            if check_up(string_list, x_pos, y_pos):
                generate_path(string_list, x_pos, y_pos - 1, 'down')
            up_tried = True
        elif try_path == 4 and not down_tried:
            if check_down(string_list, x_pos, y_pos):
                generate_path(string_list, x_pos, y_pos + 1, 'up')
            down_tried = True
    return
    


    

#generate_maze('')
