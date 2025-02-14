def getInput(filename: str):
    arr1 = []
    arr2 = []

    with open(filename, "r") as file:
        for line in file:
            input = line.split("   ")
            arr1.append(int(input[0]))
            arr2.append(int(input[1][:-1]))