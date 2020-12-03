if __name__ == '__main__':
    count = 0

    with open('AoCDay2P1.txt', 'r') as file:
        for line in file:
            password_data = line.split(' ')
            number_of_characters = password_data[0].split('-')
            low_end = int(number_of_characters[0])
            high_end = int(number_of_characters[1])
            desired_letter = password_data[1].split(':')[0]
            character_count = 0
            for letter in password_data[2]:
                if letter == desired_letter:
                    character_count += 1
            if low_end <= character_count <= high_end:
                count += 1
    print(count)
