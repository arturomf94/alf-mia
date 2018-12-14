def encode(tm):
    tm_list = []

    for instruction in tm:
        state = binary(int(instruction[0]))
        state = expand(state)
        first_symbol = simplify(instruction[1])
        tm_list.append(state)
        tm_list.append(first_symbol)
        if len(instruction) == 3:
            second_symbol = simplify(instruction[2])
            tm_list.append(second_symbol)

    tm_string = ''.join(tm_list)
    tm_string = cut(tm_string)
    natural_representation = int(tm_string, 2)

    return natural_representation

def binary(integer):
    return "{0:b}".format(integer)

def simplify(symbol):
    if symbol == '0':
        return '0'
    elif symbol == '1':
        return '10'
    elif symbol == 'R':
        return '110'
    elif symbol == 'L':
        return '1110'
    else:
        return '11110'

def expand(string):
    str = ''
    for char in string:
        str = str + simplify(char)
    return str

def cut(string):
    if len(string) >= 3:
        return string[:-3]
    else:
        return string
