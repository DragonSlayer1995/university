from collections import defaultdict

maximum_students = int(input())
temp_max_students = maximum_students
applicant = []
with open('applicant_list_5.txt') as f:
    for line in f:
        applicant.append(line.strip().split(' '))

sorted_applicant = sorted(applicant,
                          key=lambda x: (-float(x[2]), -float(x[3]), -float(x[4]), -float(x[5]), x[0] + ' ' + x[1]))

faculties = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
science_indexes = {'Biotech': 3, 'Chemistry': 3, 'Engineering': 5, 'Mathematics': 4, 'Physics': 2}
result = defaultdict(list)
i = 6
for _ in range(3):
    for faculty in faculties:
        a = len(result[faculty])
        if len(result[faculty]) >= maximum_students:
            continue
        sorted_applicant = sorted(sorted_applicant,
                                  key=lambda x: (-((float(x[2]) + float(x[3])) / 2) if faculty == 'Biotech'
                                                 else -((float(x[4]) + float(x[5])) / 2) if faculty == 'Engineering'
                                  else -((float(x[2]) + float(x[4])) / 2) if faculty == 'Physics'
                                  else -float(x[3]) if faculty == 'Chemistry'
                                  else -float(x[4]),
                                                 x[0] + ' ' + x[1]))
        faculty_list = [x for x in sorted_applicant if x[i] == faculty]
        maximum_students = maximum_students
        if len(faculty_list) > maximum_students - len(result[faculty]):
            maximum_students = maximum_students - len(result[faculty])
        faculty_list = faculty_list[:maximum_students]
        maximum_students = temp_max_students
        result[faculty].extend(faculty_list)
        sorted_applicant = [x for x in sorted_applicant if x not in faculty_list and x not in faculty_list]
    i += 1

for key, value in result.items():
    for student in value:
        if key == 'Biotech':
            student[2] = (float(student[2]) + float(student[3])) / 2
        if key == 'Engineering':
            student[2] = (float(student[4]) + float(student[5])) / 2
        if key == 'Physics':
            student[2] = (float(student[2]) + float(student[4])) / 2
        if key == 'Chemistry':
            student[2] = float(student[3])
        if key == 'Mathematics':
            student[2] = float(student[4])

for key in result.keys():
    new_list = sorted(result[key], key=lambda x: (-float(x[2]), x[0] + ' ' + x[1]))
    result[key] = new_list

for key, value in result.items():
    with open(key.lower() + '.txt', 'w', encoding='utf-8') as out_file:
        for student in value:
            out_file.write(student[0] + ' ' + student[1] + ' ' + str(student[2]) + '\n')
