from collections import defaultdict

maximum_students = int(input())
temp_max_students = maximum_students
applicant = []
with open('applicant_list_7.txt') as f:
    for line in f:
        applicant.append(line.strip().split(' '))

faculties = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
result = defaultdict(list)
i = 7
for _ in range(3):
    for faculty in faculties:
        a = len(result[faculty])
        if len(result[faculty]) >= maximum_students:
            continue
        applicant = sorted(applicant,
                                  key=lambda x: (
                                  -max(((float(x[2]) + float(x[3])) / 2), float(x[6])) if faculty == 'Biotech'
                                  else -max(((float(x[4]) + float(x[5])) / 2), float(x[6])) if faculty == 'Engineering'
                                  else -max(((float(x[2]) + float(x[4])) / 2), float(x[6])) if faculty == 'Physics'
                                  else -max(float(x[3]), float(x[6])) if faculty == 'Chemistry'
                                  else -max(float(x[4]), float(x[6])),
                                  x[0] + ' ' + x[1]))
        faculty_list = [x for x in applicant if x[i] == faculty]
        maximum_students = maximum_students
        if len(faculty_list) > maximum_students - len(result[faculty]):
            maximum_students = maximum_students - len(result[faculty])
        faculty_list = faculty_list[:maximum_students]
        maximum_students = temp_max_students
        result[faculty].extend(faculty_list)
        applicant = [x for x in applicant if x not in faculty_list and x not in faculty_list]
    i += 1

for key, value in result.items():
    for student in value:
        if key == 'Biotech':
            student[2] = max((float(student[2]) + float(student[3])) / 2, float(student[6]))
        if key == 'Engineering':
            student[2] = max((float(student[4]) + float(student[5])) / 2, float(student[6]))
        if key == 'Physics':
            student[2] = max((float(student[2]) + float(student[4])) / 2, float(student[6]))
        if key == 'Chemistry':
            student[2] = max(float(student[3]), float(student[6]))
        if key == 'Mathematics':
            student[2] = max(float(student[4]), float(student[6]))

for key in result.keys():
    new_list = sorted(result[key], key=lambda x: (-float(x[2]), x[0] + ' ' + x[1]))
    result[key] = new_list

for key, value in result.items():
    with open(key.lower() + '.txt', 'w', encoding='utf-8') as out_file:
        for student in value:
            out_file.write(student[0] + ' ' + student[1] + ' ' + str(student[2]) + '\n')
