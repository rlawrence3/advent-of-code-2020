if __name__ == '__main__':
    values = []
    found = False
    with open('AoCDay1P1.txt', 'r') as file:
        for line in file:
            value1 = int(line)
            for value2 in values:
                if value2 == value1 or value1 + value2 >= 2020:
                    continue
                for value3 in values:
                    if (value3 != value2 != value1) and value1 + value2 + value3 == 2020:
                        print(value3 * value2 * value1)
                        found = True
            if found:
                break
            else:
                values.append(value1)
