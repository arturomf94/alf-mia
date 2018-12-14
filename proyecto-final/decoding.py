def decode(natural):
    bin = binary(natural)
    uncut_bin = bin + '110'
    disentangled_keys, disentangled_values = disentangle(uncut_bin)
    disentangled_keys_string = ''.join(disentangled_keys)
    disentangled_keys_string = disentangled_keys_string.replace('RR','R00R')
    disentangled_keys_string = disentangled_keys_string.replace('1H','01H')
    disentangled_keys_string = '00R' + disentangled_keys_string
    rules = construct_rules(disentangled_keys_string)
    return rules

encoding = {
    '0': '0',
    '1': '10',
    'R': '110',
    'L': '1110',
    'H': '11110'
}

def binary(integer):
    return "{0:b}".format(integer)

def disentangle(string):
    result_values = []
    result_keys = []
    while string != '':
        first_appearance = len(string)
        key_found = ''
        for key in encoding:
            if encoding[key] in string and string.find(encoding[key]) <= first_appearance:
                first_appearance = string.find(encoding[key])
                key_found = key
        # if not encoding[key_found] in string:
        #     break
        result_values.append(encoding[key_found])
        result_keys.append(key_found)
        string = string.replace(encoding[key_found], '', 1)
    return result_keys, result_values

def construct_rules(string):
    result = []
    while string != '':
        for i in string:
            if not i.isdigit():
                index = string.find(i) - 1
                state = string[0:index]
                result.append((state, string[index], string[index + 1]))
                break
        string = string[(index + 2):]
    return result
