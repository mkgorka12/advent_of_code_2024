def getInput(filename: str):
    res = []

    with open(filename, "r") as file:
        res = file.read()

    return res

def getMulParameters(input: str):
    valid = False
    parameters = ""

    for idx, char in enumerate(input):
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