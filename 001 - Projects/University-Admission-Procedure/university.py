departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
exam_index = {'Biotech': [2, 3], 'Chemistry': [3, 3], 'Engineering': [4, 5], 'Mathematics': [4, 4], 'Physics': [2, 4]}
accepted = []
N = int(input())

with open("applicants.txt", "r") as file:
    applicants = [line.split() for line in file]

for choice in range(7, 10):
    for dept, exam in exam_index.items():
        applicants_mean = []
        for line in applicants:
            mean = (float(line[exam[0]]) + float(line[exam[1]])) / 2
            if float(line[6]) > mean:
                mean = float(line[6])
            name = [line[0], line[1], mean, line[7], line[8], line[9]]
            applicants_mean.append(name)

        applicants_mean.sort(key=lambda x: (-x[2], x[0], x[1]))
        for student in applicants_mean:
            name = student[0:2]
            if dept == student[choice - 4] and name not in accepted and len(departments[dept]) < N:
                departments[dept].append([*name, str(student[2])])
                accepted.append(name)
for department, student in departments.items():
    with open(f"{department}.txt", 'w') as file:
        for name in sorted(student, key=lambda x: (-float(x[2]), x[0], x[1])):
            file.write(' '.join(name) + '\n')
