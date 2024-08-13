import random

# Looping through a list and create a dict
# new_dict = {new_key:new_value for item in list}
# new dict name = {key of the new dict : value of the new dict || for || increment variable || in || list name}

names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Feddie"]
student_score = {student:random.randint(1,100) for student in names}
print(student_score)

# Looping through a dict and create a dict
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# new dict name = {key of the new dict : value of the new dict || for || increment variable || in || list name || if condition}

passed_student = {student:score for (student,score) in student_score.items() if score >= 60}
print(passed_student,"\n")

# _______________________________________________________________________________________________________________________________________________

import pandas

student_dict = {
    "student" : ["Nihil","Hesara","Nimadith"],
    "score" : [56,78,96]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame,"\n")

# Loop through rows of a data frame
for (index,row) in student_data_frame.iterrows():
    print(row,"\n")
    print(row.student)      # To get the students name 
    print(row.score)        # To get the score 

if row.student == "Nihil":
    print(row.score)