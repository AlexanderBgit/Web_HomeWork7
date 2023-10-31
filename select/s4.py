from sqlalchemy import func
from models2 import Grade
from db import session

def get_average_grade_for_all():
    average_grade = session.query(func.avg(Grade.grade).label('average_grade')).scalar()
    return average_grade

if __name__ == '__main__':
    average_grade_all = get_average_grade_for_all()
    print("Average grade for all: ", average_grade_all)
