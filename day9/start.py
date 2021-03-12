programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
 "Function": "A piece of code that you can easily call over and over again."
}

programming_dictionary["Hello"] = "Hello world!"
print(programming_dictionary)

for key in programming_dictionary:
    print(programming_dictionary[key])

# Excercise
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for scores in student_scores:
    if student_scores[scores] >= 91:
        student_grades[scores] = "Outstanding"
    elif student_scores[scores] > 80:
        student_grades[scores] = "Exceeds Expectations"
    elif student_scores[scores] > 70:
        student_grades[scores] = "Acceptable"
    else:
        student_grades[scores] = "Fail"
    

print(student_grades)