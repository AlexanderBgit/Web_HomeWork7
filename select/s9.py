from models2 import Student, Subject, Grade
from db import session

def courses_attended_by_student(student_id):
    student = session.query(Student).filter(Student.id == student_id).first()

    if student:
        subjects_attended = (
            session.query(Subject.subject_name)
            .join(Grade)
            .filter(Grade.student_id == student.id)
            .distinct()  # Використання distinct для унікальних значень
            .all()
        )

        if subjects_attended:
            return student.student_name, list({subject.subject_name for subject in subjects_attended})

    return None, None

# if __name__ == '__main__':
#     student_id = 25
#     student_name, student_courses = courses_attended_by_student(student_id)

#     if student_name and student_courses:
#         print(f"Student ID {student_id}, {student_name}, is attending the following courses:")
#         for course in student_courses:
#             print(course)
#     else:
#         print(f"No courses found for student ID: {student_id}")

