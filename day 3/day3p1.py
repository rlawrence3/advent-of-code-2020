def tree_check(tree_map, right_move, down_move):
    tree_count = 0
    row = 0
    column = 0
    row_length = len(tree_map[0])

    while row < len(tree_map) - 1:
        column = (column + right_move) % (row_length - 1)
        row = row + down_move
        if tree_map[row][column] == '#':
            tree_count += 1

    return tree_count


if __name__ == '__main__':
    tree_map = []

    with open('AoCDay3P1.txt', 'r') as file:
        for line in file:
            tree_map.append(line)

    print(tree_check(tree_map, 3, 1))
