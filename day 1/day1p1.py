"""
Goes through the values of AoCDay3P1.txt and finds the first pair of numbers that add up to 2020. After
those are found, the function prints the product of those two numbers to the console.
"""
if __name__ == '__main__':
    memos = []
    for num in range(2021):
        memos.append(0)

    with open('AoCDay1P1.txt', 'r') as file:
        for line in file:
            value = int(line)
            if memos[2020 - value] == 1:
                print(value * (2020 - value))
                break
            else:
                memos[value] = 1

