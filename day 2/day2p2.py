if __name__ == '__main__':
    count = 0

    with open('AoCDay2P1.txt', 'r') as file:
        for line in file:
            password_data = line.split(' ')
            number_of_characters = password_data[0].split('-')
            low_point = int(number_of_characters[0])
            high_point = int(number_of_characters[1])
            desired_letter = password_data[1].split(':')[0]
            found_once = False
            password = password_data[2]
            if password[low_point - 1] == desired_letter:
                found_once = not found_once
            if password[high_point - 1] == desired_letter:
                found_once = not found_once
            if found_once:
                count += 1
    print(count)
