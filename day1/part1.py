from common import getInput
from functools import reduce

arr1, arr2 = getInput("input.txt")

arr1.sort()
arr2.sort()

res = reduce(lambda acc, new: acc + abs(new[0] - new[1]), zip(arr1, arr2), 0)

print(res)