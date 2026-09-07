from typing import List

def read_integers() -> List[int]:
    split_input = input().split(',')
    for i in range(len(split_input)):
        split_input[i] = int(split_input[i])
    return split_input

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
