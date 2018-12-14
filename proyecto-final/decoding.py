def decode(natural):
    bin = binary(natural)
    uncut_bin = bin + '110'

    return uncut_bin

def binary(integer):
    return "{0:b}".format(integer)

import pdb; pdb.set_trace()
