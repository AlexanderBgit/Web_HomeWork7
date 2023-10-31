from models2 import Grade, Student, Subject
from db import session

def get_grades_for_group_subject(group_id, subject_id):
    grades = (
        session.query(Grade, Student.student_name)
        .join(Student)
        .filter(Student.group_id == group_id)
        .filter(Grade.subject_id == subject_id)
        .all()
    )
    return grades

if __name__ == '__main__':
    group_id = 1  # Група id=1
    subject_id = 2  # Предмет id=2
    grades = get_grades_for_group_subject(group_id, subject_id)
    for grade, student_name in grades:
        print(f"Student Name: {student_name}, Grade: {grade.grade}")
