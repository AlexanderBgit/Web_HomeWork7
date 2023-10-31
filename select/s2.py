from sqlalchemy import func, desc, select
from models2 import Student, Grade, Subject, Teacher, Group
from db import session

# from tabulate import tabulate

def select_one():
    """
    Знайти студента із найвищим середнім балом з певного предмета.
    :return: dict
    """
    subject_id = 2
    result = (session.query(
        Student.student_name,
        func.avg(Grade.grade).label('avg_grade'),
        )
        .select_from(Grade)
        .join(Student)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(desc('avg_grade'))
        .first()
    )
    return result

if __name__ == '__main__':
    print(select_one())