import re

bag_types = []
memos = []


class ContainedBag:
    def __init__(self, input_string):
        self.number = int(input_string[0])
        self.color = input_string[2:]


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
                    self.contents.append(ContainedBag(bag.strip()))


def number_of_bags(checked_bag):
    result = 0
    for bag in bag_types:
        if bag.color == checked_bag.color:
            checked_bag = bag
            break
    if len(checked_bag.contents) == 0:
        return 1
    else:
        for content in checked_bag.contents:
            result += content.number * number_of_bags(content)
    return result


if __name__ == '__main__':
    with open('AoCDay7.txt') as file:
        for line in file:
            bag_types.append(Bag(line))

    for bag in bag_types:
        if bag.color == 'shiny gold':
            print(number_of_bags(bag))
