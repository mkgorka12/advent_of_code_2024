import common

reports = common.getInput("input.txt")

# I'm not proud of this solution, however I don't know yet how to do it better

safeReports = 0
for report in reports:
    for i in range(len(report)):
        if common.isDiffOk(report[:i] + report[i + 1:]) and (common.isSortedAsc(report[:i] + report[i + 1:]) or common.isSortedDesc(report[:i] + report[i + 1:])):
            safeReports += 1
            break

print(safeReports)
