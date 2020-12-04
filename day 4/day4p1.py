import re

FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_data(field_data):
    field_name = field_data[0]

    if field_name == 'byr':
        return 1920 <= int(field_data[1]) <= 2002
    elif field_name == 'iyr':
        return 2010 <= int(field_data[1]) <= 2020
    elif field_name == 'eyr':
        return 2020 <= int(field_data[1]) <= 2030
    elif field_name == 'hgt':
        if len(field_data[1]) <= 3:
            return False
        if field_data[1][2] == 'i':
            if 59 <= int(field_data[1][0:2]) <= 76:
                return True
        elif field_data[1][3] == 'c' and 150 <= int(field_data[1][0:3]) <= 193:
            return True
        return False
    elif field_name == 'hcl':
        regex = re.compile('^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f](\n)*$')
        return re.match(regex, field_data[1])
    elif field_name == 'ecl':
        return field_data[1][0:3] in EYE_COLORS
    elif field_name == 'pid':
        regex = re.compile('^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9](\n)*$')
        return re.match(regex, field_data[1])
    else:
        return True


def passport_check(passport):
    cid_found = False
    field_count = 0
    passport_data = passport.split(' ')
    for field in passport_data:
        field_data = field.split(':')
        field_checked = field_data[0]
        if field_checked in FIELDS and validate_data(field_data):
            field_count += 1
        if field_checked == 'cid':
            cid_found = True
    return [field_count, cid_found]


if __name__ == '__main__':
    valid_passports = 0
    with open('AoCDay4P1.txt') as file:
        passport = ''
        for line in file:
            if line != '\n':
                passport += ' ' + line
            else:
                passport_data = passport_check(passport)
                if passport_data[0] == 8 or (passport_data[0] == 7 and not passport_data[1]):
                    valid_passports += 1
                passport = ''

    print(valid_passports)
