students = {}

def add_student(roll_number, name):
  students[roll_number] = name

def display_student(roll_number):
  if roll_number in students:
    print(f"Student name: {students[roll_number]}")
  else:
    print("Student not found")

def search_student(name):
  for roll_number, student_name in students.items():
    if student_name == name:
      print(f"Roll number: {roll_number}")
      return
  print("Student not found")

def delete_student(roll_number):
  if roll_number in students:
    del students[roll_number]
    print("Student deleted successfully")
  else:
    print("Student not found")

def update_student(roll_number, name):
  if roll_number in students:
    students[roll_number] = name
    print("Student updated successfully")
  else:
    print("Student not found")

# Test the functions
add_student(1, "John Smith")
add_student(2, "Jane Smith")

display_student(1)
# Output: "Student name: John Smith"

search_student("John Smith")
# Output: "Roll number: 1"

delete_student(2)

update_student(1, "John Doe")
display_student(1)
# Output: "Student name: John Doe"