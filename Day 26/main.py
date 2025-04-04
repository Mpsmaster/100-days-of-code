import random
numbers = [1, 2, 3]
new_number = [n + 1 for n in numbers]
print(new_number)
name = "Marco"
new_list = [letter for letter in name]
print(new_list)

new_range = [n * 2 for n in range(1, 5)]
print(new_range)
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
upper_names = [upname.upper() for upname in names if len(upname) > 4] 
print(upper_names)

students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)