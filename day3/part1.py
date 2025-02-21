import common

input = common.getInput("/home/mkgorka/Documents/advent_of_code_2024/day3/input.txt")

res = 0
mulBMT = common.BadMatchTable("mul")

for i in range(len(input)):
    if input[i:i+3] == "mul":
        res += common.multiplyMulParameters(input[i+3:i+12])
    else:
        i += mulBMT.offset(input[i])

print(res)