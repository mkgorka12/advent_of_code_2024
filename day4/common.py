def getInput(filename: str):
    input = []
    
    with open(filename, "r") as file:
        for line in file:
            row = []   
            for char in line:
                if char == '\n':
                    break
                row.append(char)
            input.append(row)

    return input

def checkUp(matrix: list[list[str]], searched: str, offset: tuple[int,int]):
    res = ""
    for i in range(len(searched)):
        if offset[0] - i >= 0:
            res += matrix[offset[0] - i][offset[1]]

    if res == searched:
        return True
    return False

def checkDown(matrix: list[list[str]], searched: str, offset: tuple[int,int]):
    height = len(matrix)
    res = ""
    for i in range(len(searched)):
        if offset[0] + i < height:
            res += matrix[offset[0] + i][offset[1]]

    if res == searched:
        return True
    return False

def checkRight(matrix: list[list[str]], searched: str, offset: tuple[int,int]):
    width = len(matrix[0])
    if len(searched) + offset[1] - 1 < width and "".join(matrix[offset[0]][offset[1]:offset[1]+len(searched)]) == searched:
        return True
    return False

def checkLeft(matrix: list[list[str]], searched: str, offset: tuple[int, int]) -> bool:
    if offset[1] - len(searched) + 1 >= 0 and "".join(matrix[offset[0]][offset[1]-len(searched)+1:offset[1]+1]) == searched[::-1]:
        return True
    return False

def checkDiagonalUpRight(matrix: list[list[str]], searched: str, offset: tuple[int,int]):
    width = len(matrix[0])
    res = ""
    for i in range(len(searched)):
        if offset[0] - i >= 0 and offset[1] + i < width:
            res += matrix[offset[0] - i][offset[1] + i]

    if res == searched:
        return True
    return False

def checkDiagonalUpLeft(matrix: list[list[str]], searched: str, offset: tuple[int,int]):
    res = ""
    for i in range(len(searched)):
        if offset[0] - i >= 0 and offset[1] - i >= 0:
            res += matrix[offset[0] - i][offset[1] - i]

    if res == searched:
        return True
    return False

def checkDiagonalDownRight(matrix: list[list[str]], searched: str, offset: tuple[int,int]):
    height = len(matrix)
    width = len(matrix[0])
    res = ""
    for i in range(len(searched)):
        if offset[0] + i < height and offset[1] + i < width:
            res += matrix[offset[0] + i][offset[1] + i]

    if res == searched:
        return True
    return False

def checkDiagonalDownLeft(matrix: list[list[str]], searched: str, offset: tuple[int,int]):
    height = len(matrix)
    res = ""
    for i in range(len(searched)):
        if offset[0] + i < height and offset[1] - i >= 0:
            res += matrix[offset[0] + i][offset[1] - i]

    if res == searched:
        return True
    return False

def checkAllDirections(matrix: list[list[str]], searched: str, offset: tuple[int, int]):
    checkFunctions = [
        checkUp, checkDown, checkRight, checkLeft,
        checkDiagonalUpRight, checkDiagonalUpLeft,
        checkDiagonalDownLeft, checkDiagonalDownRight
    ]
    
    return sum(func(matrix, searched, offset) for func in checkFunctions)