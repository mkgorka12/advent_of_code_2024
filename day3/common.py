def getInput(filename: str):
    res = []

    with open(filename, "r") as file:
        res = file.read()

    return res

def multiplyMulParameters(input: str):
    if input[0] != '(':
        return 0

    valid = False
    parameters = ""

    for idx, char in enumerate(input[1:]):
        if char == ')':
            valid = True
            break
        elif idx >= 8:
            break

        parameters += char

    if valid:
        try:
            parameters = list(map(int, parameters.split(',')))
            return parameters[0] * parameters[1] if len(parameters) == 2 else 0
        except:
            return 0
        
    return 0

class BadMatchTable:
    def __init__(self, string: str):
        self.strlen = len(string)
        self.dict = {}

        for idx, char in enumerate(string):
            self.dict[char] = self.strlen - idx - 1

    def offset(self, char: str):
        return self.dict[char] if char in self.dict.keys() else self.strlen