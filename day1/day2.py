import csv

reports = list(csv.reader(open("./input.txt"), delimiter=" "))

left_reports = [int(r[0]) for r in reports]
right_reports = [int(r[1]) for r in reports]

similarity_scores = {l: 0 for l in left_reports}

for r in right_reports:
    if r in similarity_scores:
        similarity_scores[r] = similarity_scores[r] + 1

final_score = sum(l * similarity_scores[l] for l in left_reports)

print(final_score)
