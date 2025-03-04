import common

reports = common.getInput("input.txt")

safeReports = 0
for report in reports:
    if common.isDiffOk(report) and (common.isSortedAsc(report) or common.isSortedDesc(report)):
        safeReports += 1

print(safeReports)
