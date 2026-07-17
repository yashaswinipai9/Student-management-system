from student import (
    students,
    add_student,
    remove_student,
    search_student,
    update_student,
    export_students
)

def setup_function():
    students.clear()

def test_add_student():
    result = add_student(101, "Rahul", 20)

    assert result == "Student added successfully."
    assert 101 in students

def test_add_duplicate_student():
    add_student(101, "Rahul", 20)

    result = add_student(101, "Rahul", 20)

    assert result == "Student already exists."

def test_remove_student():
    add_student(101, "Rahul", 20)

    result = remove_student(101)

    assert result == "Student removed successfully."
    assert 101 not in students

def test_remove_non_existing_student():
    result = remove_student(999)

    assert result == "Student not found."

def test_search_existing_student():
    add_student(101, "Rahul", 20)

    result = search_student(101)

    assert result == {
        "name": "Rahul",
        "age": 20
    }

def test_search_non_existing_student():
    result = search_student(999)

    assert result == "Student not found."

def test_update_existing_student():
    add_student(101, "Rahul", 20)

    result = update_student(101, "Rahul Sharma", 21)

    assert result == "Student updated successfully."

    assert students[101]["name"] == "Rahul Sharma"
    assert students[101]["age"] == 21

def test_update_non_existing_student():
    result = update_student(999, "ABC", 25)

    assert result == "Student not found."

def test_add_multiple_students():
    add_student(101, "Rahul", 20)
    add_student(102, "Priya", 21)

    assert len(students) == 2

def test_verify_updated_student():
    add_student(101, "Rahul", 20)

    update_student(101, "Rahul Sharma", 22)

    result = search_student(101)

    assert result["name"] == "Rahul Sharma"
    assert result["age"] == 22

def test_export_students():
    add_student(101, "Rahul", 20)
    add_student(102, "Priya", 21)

    result = export_students()

    assert len(result) == 2
    assert result[101]["name"] == "Rahul"
    assert result[102]["name"] == "Priya"