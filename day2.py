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

from collections import Counter

def is_safe_tolerate_one_exception(report, VALID_LEVEL_CHANGE):
    # iterating through report

    for i in range(0, len(report) - 1):
        # check if its safe

        diff = abs(report[i + 1] - report[i])

        if  diff == 0 or diff > VALID_LEVEL_CHANGE:
            # check if report minus first checked value is ok

            report_minus_i = report.copy()
            report_minus_i.pop(i)

            is_ok = True
            for j in range(0, len(report_minus_i) - 1):
                diff = abs(report_minus_i[j + 1] - report_minus_i[j])

                if diff == 0 or diff > VALID_LEVEL_CHANGE:
                    is_ok = False
                    break

            if is_ok and (report_minus_i == sorted(report_minus_i) or report_minus_i == sorted(report_minus_i, reverse=True)):
                return True
            
            # check if report minus first checked value is ok

            report_minus_imore = report.copy()
            report_minus_imore.pop(i + 1)

            is_ok = True
            for j in range(0, len(report_minus_imore) - 1):
                diff = abs(report_minus_imore[j + 1] - report_minus_imore[j])

                if diff == 0 or diff > VALID_LEVEL_CHANGE:
                    is_ok = False
                    break

            if is_ok and (report_minus_imore == sorted(report_minus_imore) or report_minus_imore == sorted(report_minus_imore, reverse=True)):
                return True
            
            return False
        
    if report == sorted(report) or report == sorted(report, reverse=True):
        return True
    
    hist = Counter(report)

    for value, occ in hist.items():
        if occ == 3:
            return False
        elif occ == 2:
            report_minus_first_occ = report.copy()
            report_minus_first_occ.remove(value)

            report_minus_second_occ = report.copy()
            report_minus_second_occ.reverse()
            report_minus_second_occ.remove(value)
            report_minus_second_occ.reverse()

            is_ok = True
            for i in range(0, len(report_minus_first_occ) - 1):
                diff = abs(report_minus_first_occ[i + 1] - report_minus_first_occ[i])

                if diff == 0 or diff > VALID_LEVEL_CHANGE:
                    is_ok = False
                    break

            if is_ok and (report_minus_first_occ == sorted(report_minus_first_occ) or report_minus_first_occ == sorted(report_minus_first_occ, reverse=True)):
                return True
            
            is_ok = True
            for i in range(0, len(report_minus_second_occ) - 1):
                diff = abs(report_minus_second_occ[i + 1] - report_minus_second_occ[i])

                if diff == 0 or diff > VALID_LEVEL_CHANGE:
                    is_ok = False
                    break

            if is_ok and (report_minus_second_occ == sorted(report_minus_second_occ) or report_minus_second_occ == sorted(report_minus_second_occ, reverse=True)):
                return True
            
    return False
    
print(safe_reports(reactor_data, is_safe_tolerate_one_exception, 3))
