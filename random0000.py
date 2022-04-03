import random

def random(num_length):
    str_bupper = ''
    while num_length > 0:
        str_bupper += f'{random.randrange(0, 10)}'
        num_length -= 1
    return str_bupper














