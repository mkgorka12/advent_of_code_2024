def getInput(filename: str):
    res = []

    with open(filename, "r") as file:
        for line in file:
            report = list(map(int, line.split(" ")))
            res.append(report)

    return res

def isSortedAsc(report: list):
    for i in range(len(report) - 1):
        if report[i + 1] - report[i] < 0:
            return False
        
    return True

def isSortedDesc(report: list):
    for i in range(len(report) - 1):
        if report[i + 1] - report[i] > 0:
            return False
        
    return True

def isDiffOk(report: list):
    for i in range(len(report) - 1):
        diff = abs(report[i + 1] - report[i])
        if diff < 1 or diff > 3:
            return False
        
    return True