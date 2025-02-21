import common
from collections import Counter
from functools import reduce

arr1, arr2 = common.getInput("input.txt")

counter = Counter(arr2)

similarityScore = map(lambda x: x * counter[x], arr1)

print(sum(similarityScore))