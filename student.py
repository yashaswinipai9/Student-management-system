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

