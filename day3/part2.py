import common

input = common.getInput("input.txt")

res = 0
enabled = True

mulBMT = common.BadMatchTable("mul")
doBMT = common.BadMatchTable("do()")
dontBMT = common.BadMatchTable("don't()")

for i in range(len(input)):
    if input[i:i+4] == "do()":
        enabled = True
    elif input[i:i+7] == "don't()":
        enabled = False
    elif enabled and input[i:i+3] == "mul":
        res += common.multiplyMulParameters(input[i+3:i+12])
    else:
        i += min(mulBMT.offset(input[i]), doBMT.offset(input[i]), dontBMT.offset(input[i]))

print(res)
