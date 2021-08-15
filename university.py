from collections import defaultdict

maximum_students = int(input())
applicant = []
with open('applicant_list.txt') as f:
    for line in f:
        applicant.append(line.strip().split(' '))

sorted_applicant = sorted(applicant, key=lambda x: (-float(x[2]), x[0] + ' ' + x[1]))

faculties = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']

result = defaultdict(list)
i = 3
for _ in range(3):
    for faculty in faculties:
        if len(result[faculty]) >= maximum_students:
            continue
        faculty_list = [x for x in sorted_applicant if x[i] == faculty]
        maximum_students = maximum_students
        if len(faculty_list) > maximum_students - len(result[faculty]):
            maximum_students = maximum_students - len(result[faculty])
        faculty_list = faculty_list[:maximum_students]
        result[faculty].extend(faculty_list)
        sorted_applicant = [x for x in sorted_applicant if x not in faculty_list and x not in faculty_list]
    i += 1

for key in result.keys():
    new_list = sorted(result[key], key=lambda x: -float(x[2]))
    result[key] = new_list

for key, value in result.items():
    print(key)
    for student in value:
        print(student[0], student[1], student[2])
    print()