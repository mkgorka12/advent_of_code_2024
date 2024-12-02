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
        if safe_condition(report, VALID_LEVEL_CHANGE):
            safe_reports_counter += 1

    return safe_reports_counter

reactor_data = []

with open("example.txt", "r") as file:
    for line in file:
        reactor_data.append([int(x) for x in line.split()])

print(safe_reports(reactor_data, is_safe, 3))

# PART 2
# doesnt work (540 is not the answear at least for me)

from collections import Counter

def pop_last_occ(report, num):
    for i in range(len(report) - 1, -1, -1):
        if report[i] == num:
            report.pop(i)
            break

def check_asc_order(report, VALID_LEVEL_CHANGE):
    # check duplicates  
    duplicates = Counter(report)
    popped = False
    
    for num, occ in duplicates.items():
        if occ == 2 and not popped:
            idx = report.index(num)

            if report[idx] > report[idx + 1]:
                report.pop(idx)
            else:
                pop_last_occ(report, report[idx])

            popped = True
        elif occ >= 3 or (occ == 2 and popped):
            return False

    # check order
    report_asc = sorted(report)

    for i in range(len(report)):
        if report[i] != report_asc[i] and not popped:
            if report[i] > report[i + 1]:
                report_asc.remove(report[i])
                report.pop(i)
            else:
                pop_last_occ(report_asc, report[i])
                pop_last_occ(report, report[i])
                
            popped = True

            for j in range(len(report)):
                if report[j] != report_asc[j]:
                    return False
                
            break
        elif report[i] != report_asc[i] and popped:
            return False

    # check difference
    for i in range(1, len(report)):      

        diff = abs(report[i] - report[i - 1])

        if (diff > VALID_LEVEL_CHANGE or diff == 0) and not popped:

            if i + 1 < len(report):
                if abs(report[i + 1] - report[i]) <= VALID_LEVEL_CHANGE and abs(report[i + 1] - report[i]) > 0:
                    report.pop(i - 1)
                else:
                    report.pop(i)
            else:
                if abs(report[i - 1] - report[i - 2]) <= VALID_LEVEL_CHANGE and abs(report[i - 1] - report[i - 2]) > 0:
                    report.pop(i)
                else:
                    report.pop(i - 1)

            popped = True

            for j in range(1, len(report)):

                diff = abs(report[j] - report[j - 1])

                if (diff > VALID_LEVEL_CHANGE or diff == 0):
                    return False
                
            break
        elif (diff > VALID_LEVEL_CHANGE or diff == 0) and popped:
            return False

    return True

def check_desc_order(report, VALID_LEVEL_CHANGE):
    # check duplicates  
    duplicates = Counter(report)
    popped = False
    
    for num, occ in duplicates.items():
        if occ == 2 and not popped:
            i = report.index(num)

            if report[i] > report[i + 1]:
                pop_last_occ(report, report[i])
            else:
                report.pop(i)

            popped = True
        elif occ >= 3 or (occ == 2 and popped):
            return False

    # check order
    report_desc = sorted(report, reverse=True)

    for i in range(len(report)):
        if report[i] != report_desc[i] and not popped:
            if report[i] > report[i + 1]:
                pop_last_occ(report_desc, report[i])
                pop_last_occ(report, report[i])
            else:
                report_desc.remove(report[i])
                report.pop(i)

            popped = True

            for j in range(len(report)):
                if report[j] != report_desc[j]:
                    return False

            break
        elif report[i] != report_desc[i] and popped:
            return False

    # check difference
    for i in range(1, len(report)):      

        diff = abs(report[i] - report[i - 1])

        if (diff > VALID_LEVEL_CHANGE or diff == 0) and not popped:

            if i + 1 < len(report):
                if abs(report[i + 1] - report[i]) <= VALID_LEVEL_CHANGE and abs(report[i + 1] - report[i]) > 0:
                    report.pop(i - 1)
                else:
                    report.pop(i)
            else:
                if abs(report[i - 1] - report[i - 2]) <= VALID_LEVEL_CHANGE and abs(report[i - 1] - report[i - 2]) > 0:
                    report.pop(i)
                else:
                    report.pop(i - 1)

            popped = True

            for j in range(1, len(report)):

                diff = abs(report[j] - report[j - 1])

                if (diff > VALID_LEVEL_CHANGE or diff == 0):
                    return False
                
            break
        elif (diff > VALID_LEVEL_CHANGE or diff == 0) and popped:
            return False

    return True

def is_safe_tolerate_one_exception(report, VALID_LEVEL_CHANGE):
    if is_safe(report, VALID_LEVEL_CHANGE):
        return True
        
    asc_result = check_asc_order(report.copy(), VALID_LEVEL_CHANGE)
    desc_result = check_desc_order(report.copy(), VALID_LEVEL_CHANGE)

    return asc_result or desc_result
    
print(safe_reports(reactor_data, is_safe_tolerate_one_exception, 3))
