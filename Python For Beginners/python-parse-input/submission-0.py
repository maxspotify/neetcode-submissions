from typing import List

def read_integers() -> List[int]:
    my_input = input()
    split_input = my_input.split(',')
    new_arr = []
    for char in split_input:
        new_arr.append(int(char))
    return new_arr


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
