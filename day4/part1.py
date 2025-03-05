import common

searched = "XMAS"
matrix = common.getInput("c:/Users/Maciej/Documents/vsc PY/advent_of_code_2024/day4/input.txt")

res = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        res += common.checkAllDirections(matrix, searched, (i, j))

print(res)