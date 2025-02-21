import common

input = common.getInput("/home/mkgorka/Documents/advent_of_code_2024/day3/input.txt")
res = 0

for i in range(len(input)):
    if input[i:i+4] == "mul(":
        res += common.getMulParameters(input[i+4:i+13])

print(res)