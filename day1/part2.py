from common import getInput
from collections import Counter
from functools import reduce

arr1, arr2 = getInput("/home/mkgorka/Documents/advent_of_code_2024/day1/input.txt")

counter = Counter(arr2)

similarityScore = map(lambda x: x * counter[x], arr1)

print(sum(similarityScore))