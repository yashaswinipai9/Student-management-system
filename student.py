students = {}

def add_student(student_id, name, age):
    """
    Adds a new student to the student dictionary.
    """

    if student_id in students:
        return "Student already exists."

    students[student_id] = {
        "name": name,
        "age": age
    }

    return "Student added successfully."

def remove_student(student_id):
    if student_id not in students:
        return "Student not found."

    del students[student_id]

    return "Student removed successfully."

def search_student(student_id):
    """
    Searches for a student by ID.
    Returns the student details if found,
    otherwise returns 'Student not found.'
    """

    return students.get(student_id, "Student not found.")
   

def update_student(student_id, name, age):
    if student_id not in students:
        return "Student not found."

    students[student_id]["name"] = name
    students[student_id]["age"] = age

    return "Student updated successfully."
