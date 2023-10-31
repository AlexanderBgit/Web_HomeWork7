from sqlalchemy import func, desc, select
from models2 import Student, Grade, Subject, Teacher, Group
from db import session

# from tabulate import tabulate

def select_one():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    :return: list[dict]
    """
    result = (session.query(
        Student.student_name,
        func.avg(Grade.grade).label('avg_grade'),
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc('avg_grade'))
        .limit(5).all()
    )
    return result

if __name__ == '__main__':
    print(select_one())