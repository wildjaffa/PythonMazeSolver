def generate_maze(fileName):
    string_list = list()
    for i in range(10):
        row = '1111111111'
        string_list.append(row)
    #string_list[0][5] = '0'
    string_list[0] = flip_bit(string_list[0], 5)
    print(string_list[0])

def flip_bit(row, num):
    ret = row[0 : num] + '0' + row[num + 1 : 10]
    return ret

generate_maze('')