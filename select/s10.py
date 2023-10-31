from sqlalchemy import and_
from models2 import Student, Subject, Grade, Teacher
from db import session

def courses_taught_by_teacher_to_student(teacher_id, student_id):
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
    student = session.query(Student).filter(Student.id == student_id).first()

    if teacher and student:
        courses_taught = (
            session.query(Subject.subject_name)
            .join(Grade)
            .join(Student)
            .join(Teacher)
            .filter(and_(Teacher.id == teacher_id, Student.id == student_id))
            .distinct()  # Використання distinct для унікальних значень
            .all()
        )

        if courses_taught:
            return teacher.teacher_name, student.student_name, list({course.subject_name for course in courses_taught})

    return None, None, None

# if __name__ == '__main__':
#     teacher_id = 2
#     student_id = 25

#     teacher_name, student_name, courses_taught = courses_taught_by_teacher_to_student(teacher_id, student_id)

#     if teacher_name and student_name and courses_taught:
#         print(f"Teacher {teacher_name}, teaches the following courses to Student {student_name}:")
#         for course in courses_taught:
#             print(course)
#     else:
#         print(f"No courses found taught by Teacher ID {teacher_id} to Student ID {student_id}")
