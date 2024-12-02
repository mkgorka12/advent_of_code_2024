# PART 1

def is_level_change_valid(level_change, is_lvl_increasing, VALID_LEVEL_CHANGE):
    if is_lvl_increasing:
        return level_change > 0 and level_change <= VALID_LEVEL_CHANGE
    else:
        return level_change < 0 and level_change >= -VALID_LEVEL_CHANGE

def is_safe(report, VALID_LEVEL_CHANGE):
    is_lvl_increasing = report[1] - report[0] > 0

    for i in range(1, len(report)):
        level_change = report[i] - report[i - 1]

        if is_level_change_valid(level_change, is_lvl_increasing, VALID_LEVEL_CHANGE) is False:
            return False
        
    return True

def safe_reports(reactor_data, safe_condition, VALID_LEVEL_CHANGE):
    safe_reports_counter = 0
    
    for report in reactor_data:
        print(report, end=" ")
        if safe_condition(report, VALID_LEVEL_CHANGE):
            print("safe")
            safe_reports_counter += 1
        else:
            print("not safe")

    return safe_reports_counter

reactor_data = []

with open("example.txt", "r") as file:
    for line in file:
        reactor_data.append([int(x) for x in line.split()])

print(safe_reports(reactor_data, is_safe, 3))

# PART 2

#def is_safe_tolerate_one_exception(report, VALID_LEVEL_CHANGE)
#print(safe_reports(reactor_data, is_safe_tolerate_one_exception, 3))

