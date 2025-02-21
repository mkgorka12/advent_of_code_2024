import common
from functools import reduce

arr1, arr2 = common.getInput("input.txt")

arr1.sort()
arr2.sort()

res = reduce(lambda acc, new: acc + abs(new[0] - new[1]), zip(arr1, arr2), 0)

print(res)