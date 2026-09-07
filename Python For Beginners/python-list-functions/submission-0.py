from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    my_sum = 0
    for num in nums:
        my_sum += num
    return my_sum

def get_min(nums: List[int]) -> int:
    if not nums:
        return None

    my_min = nums[0]
    for num in nums:
        if num < my_min:
            my_min = num
    return my_min


def get_max(nums: List[int]) -> int:
    if not nums:
        return None
    
    my_max = nums[0]
    for num in nums:
        if num > my_max:
            my_max = num
    return my_max

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
