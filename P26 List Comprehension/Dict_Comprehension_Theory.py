# Looping through a list and create a dict
# new_dict = {new_key:new_value for item in list}
# new dict name = {key of the new dict : value of the new dict || for || increment variable || in || list name}

# Looping through a dict and create a dict
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# new dict name = {key of the new dict : value of the new dict || for || increment variable || in || list name || if condition}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Feddie"]
student_score = {student:random.randint(1,100) for student in names}
print(student_score)

passed_student = {student:score for (student,score) in student_score.items() if score >= 60}
print(passed_student)