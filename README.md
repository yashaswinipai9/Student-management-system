# Student Management System

## Project Description

This project is a simple Student Management System developed in Python. It allows users to add, remove, search, and update student records using a Python dictionary.

## Project Structure

```
student-management-system/
│── student.py
│── test_student.py
│── requirements.txt
│── README.md
└── .github/
    └── workflows/
        └── python.yml
```

## Features

- Add student
- Remove student
- Search student
- Update student

## Requirements

- Python 3.x
- pytest

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the tests:

```bash
pytest
```

## Git Commands Used

```bash
git init
git status
git add .
git commit -m "Commit message"
git branch -M main
git remote add origin <repository-url>
git push -u origin main
git checkout -b feature-student-search
git push -u origin feature-student-search
git log --oneline
git pull origin main
```

## GitHub Actions Workflow

The GitHub Actions workflow automatically runs pytest whenever code is pushed to the repository or when a Pull Request is created.

The workflow:
- Checks out the repository
- Installs Python
- Installs project dependencies
- Executes pytest
- Reports success or failure automatically

## Author

Yashaswini Pai