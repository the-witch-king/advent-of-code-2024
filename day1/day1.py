import csv

reports = list(csv.reader(open("./input.txt"), delimiter=" "))

left_reports = sorted([int(r[0]) for r in reports])
right_reports = sorted([int(r[1]) for r in reports])

ordered_reports = zip(left_reports, right_reports)

result = sum([abs(int(r[0]) - int(r[1])) for r in ordered_reports])

print(result)
