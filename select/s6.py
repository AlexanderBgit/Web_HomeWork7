from models2 import Student, Group
from db import session

def get_students_in_group(group_id):
    students = session.query(Student).filter(Student.group_id == group_id).all()
    return students

if __name__ == '__main__':
    group_id = 1  # Група id=1
    students_in_group = get_students_in_group(group_id)
    for student in students_in_group:
        print(student.student_name)
