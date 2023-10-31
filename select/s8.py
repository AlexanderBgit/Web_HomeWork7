from sqlalchemy import func
from models2 import Grade, Teacher, Subject
from db import session

def average_grade_by_teacher(teacher_id):
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()

    if teacher:
        average_grade = session.query(
            func.avg(Grade.grade).label('average_grade')
        ).join(Subject).filter(Subject.teacher_id == teacher_id).first()

        if average_grade:
            return teacher.teacher_name, average_grade[0]

    return None, None

if __name__ == '__main__':
    teacher_id = 3  # Викладач id=3
    teacher_name, average_grade = average_grade_by_teacher(teacher_id)

    if teacher_name and average_grade:
        print(f"Teacher Name: {teacher_name}, Average Grade: {average_grade}")
    else:
        print(f"No data found for Teacher {teacher_id}")
