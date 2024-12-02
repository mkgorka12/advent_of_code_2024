# PART 1
def get_input():
    arr1 = []
    arr2 = []

    while (1):
        str_in = input("> ")

        if (str_in == ""):
            break
                
        numbers = str_in.split()

        arr1.append(int(numbers[0])) 
        arr2.append(int(numbers[1]))

    arr1.sort()
    arr2.sort()
    return [arr1, arr2]

def display(arr):
    for x in arr:
        print(x, " ", end="")

    print("")


def count_distance(arr1, arr2):
    distance = 0

    for i in range(0, len(arr1)):
        distance += abs(arr1[i] - arr2[i])

    return distance

[arr1, arr2] = get_input()
print(count_distance(arr1, arr2))

# PART 2
def count_distance_with_occurences(arr1, arr2):
    distance = 0

    for num in arr1:
        occurences = 0
        
        for x in arr2:
            if x == num:
                occurences += 1

        distance += num * occurences

    return distance

print(count_distance_with_occurences(arr1, arr2))