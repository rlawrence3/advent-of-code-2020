import re

bag_types = []
memos = []


class Bag:
    def __init__(self, input_string):
        regex = re.compile(' bag[s]?[,\.]')
        bag_data = input_string.split(' bags contain ')
        self.color = bag_data[0]
        contents = re.split(regex, bag_data[1])
        self.contents = []
        if contents[0].strip() != 'no other':
            for bag in contents:
                if len(bag) > 1:
                    self.contents.append(bag[2:].strip())


def check_contents(checked_bag):
    result = False
    if checked_bag in memos:
        return True
    elif 'shiny gold' in checked_bag.contents:
        return True
    elif len(checked_bag.contents) == 0:
        return False
    else:
        for content in checked_bag.contents:
            for bag in bag_types:
                if bag.color == content:
                    content = bag
            result = result or check_contents(content)
        return result


if __name__ == '__main__':
    valid_bags = 0
    with open('AoCDay7.txt') as file:
        for line in file:
            bag_types.append(Bag(line))

    for bag in bag_types:
        if check_contents(bag):
            valid_bags += 1

    print(valid_bags)


