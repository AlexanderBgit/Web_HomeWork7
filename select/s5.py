from models2 import Subject, Teacher
from db import session

def select_courses_by_teacher_id(teacher_id):
    """
    Знайти курси, які читає викладач за ID.
    :param teacher_id: ID викладача
    """
    courses_taught_by_teacher = (
        session.query(Subject.subject_name)
        .join(Subject.teacher)
        .filter(Teacher.id == teacher_id)
        .all()
    )

    if courses_taught_by_teacher:
        print(f"Courses taught by teacher with ID {teacher_id}:")
        for course in courses_taught_by_teacher:
            print(course.subject_name)
    else:
        print(f"No courses found for teacher with ID {teacher_id}")

if __name__ == '__main__':
    select_courses_by_teacher_id(1)  # Замість числа 1 вкажіть ID викладача
