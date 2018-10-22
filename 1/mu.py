
# MU System

ax = 'MI'

derived_strings = []
non_derived_strings = [ax]

def rule1(current_string):
    if 'I' == current_string[len(current_string) - 1]:
        new_string = current_string + 'U'
        return new_string
    else:
        return ''

def rule2(current_string):
    if 'M' == current_string[0]:
        new_string = current_string + current_string[1:]
        return new_string
    else:
        return ''

def rule3(current_string):
    if 'III' in current_string:
        new_string = current_string.replace('III', 'U')
        return new_string
    else:
        return ''

def rule4(current_string):
    if 'UU' in current_string:
        new_string = current_string.replace('UU', '')
        return new_string
    else:
        return ''

def derive_string(current_string):
    new_string = rule1(current_string)
    if new_string != '' and not(new_string in all_strings):
        non_derived_strings.append(new_string)
    new_string = rule2(current_string)
    if new_string != '' and not(new_string in all_strings):
        non_derived_strings.append(new_string)
    new_string = rule3(current_string)
    if new_string != '' and not(new_string in all_strings):
        non_derived_strings.append(new_string)
    new_string = rule4(current_string)
    if new_string != '' and not(new_string in all_strings):
        non_derived_strings.append(new_string)
    non_derived_strings.remove(current_string)
    derived_strings.append(current_string)

objective_string = raw_input()

all_strings = derived_strings + non_derived_strings

while not (objective_string in all_strings or 5000 < len(all_strings)):
            if non_derived_strings != '':
                derive_string(non_derived_strings[0])
            all_strings = derived_strings + non_derived_strings

if objective_string in all_strings:
    print(all_strings)
else:
    print('No es teorema.')
