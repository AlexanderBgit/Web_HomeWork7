from sqlalchemy import func
from models2 import Group, Student, Grade, Subject
from db import session

def get_average_grade_by_group_for_subject(subject_id):
    query = session.query(
        Group.group_name,
        func.avg(Grade.grade).label('average_grade')
    ).select_from(Group). \
        join(Student). \
        join(Grade). \
        join(Subject). \
        filter(Subject.id == subject_id). \
        group_by(Group.group_name). \
        all()

    return query

if __name__ == '__main__':
    subject_id = 2  # Предмет id=2
    average_grade_by_group = get_average_grade_by_group_for_subject(subject_id)
    print(average_grade_by_group)
