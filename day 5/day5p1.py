import math


class Seat:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.seatID = row * 8 + column


def get_seat(line):
    low_row = 0
    high_row = 127

    low_column = 0
    high_column = 7
    for character in line:
        if character == 'B':
            low_row = math.ceil((high_row + low_row) / 2)
        elif character == 'F':
            high_row = math.floor((high_row + low_row) / 2)
        elif character == 'R':
            low_column = math.ceil((high_column + low_column) / 2)
        elif character == 'L':
            high_column = math.floor((high_column + low_column) / 2)
    return Seat(low_row, low_column)


if __name__ == '__main__':
    seatIDs = []
    with open('AoCDay5.txt') as file:
        for line in file:
            seat = get_seat(line)
            seatIDs.append(seat.seatID)
    print(max(seatIDs))
