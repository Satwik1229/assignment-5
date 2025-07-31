student_marks={'Alice':'85', 'mike':'55', 'nick':'75'}
key=(input("Enter the student's name: "))
if key in student_marks:
    print(f"{key}'s marks are: {student_marks[key]}")
else:
    print("student not found.")