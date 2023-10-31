from faker import Faker
import random
from datetime import datetime, timedelta
from models2 import Student, Group, Teacher, Subject, Grade, Base
from db import session

import logging

import sys
import os

# project_root = os.path.dirname(os.path.abspath(__file__))
# src_path = os.path.join(project_root, 'src')
# sys.path.append(src_path)

# Отримання шляху до поточного файлу
current_file_path = os.path.abspath(__file__)
# Шлях до теки з файлом db.py
new_project_root = os.path.dirname(current_file_path)
sys.path.append(new_project_root)


fake = Faker('uk_UA')
try:
    if __name__ == '__main__':
        groups = ['G1', 'G2', 'G3']
        for group_name in groups:
            group = Group(group_name=group_name)
            session.add(group)
            session.commit()

        for _ in range(50):
            student_name = fake.name()
            group_id = random.randint(1, 3)
            student = Student(student_name=student_name, group_id=group_id)
            session.add(student)
            session.commit()

        for _ in range(3):
            teacher_name = fake.name()
            teacher = Teacher(teacher_name=teacher_name)
            session.add(teacher)
            session.commit()

        subjects = ['S1', 'S2', 'S3', 'S4', 'S5']
        for subject_name in subjects:
            teacher_id = random.randint(1, 3)
            subject = Subject(subject_name=subject_name, teacher_id=teacher_id)
            session.add(subject)
            session.commit()

        for student_id in range(1, 51):
            for gr in range(20):
                grade = Grade(student_id=student_id,
                            subject_id=random.randint(1, 5),
                            grade=random.randint(1, 100),
                            date=datetime.now()-timedelta(random.randint(1, 200))
                            )
                session.add(grade)
                session.commit()

        session.close()        
except Exception as e:
        logging.error(f'Помилка: {str(e)}')