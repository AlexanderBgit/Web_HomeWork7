from sqlalchemy import func, desc, select, and_
from models2 import Student, Grade, Subject, Teacher, Group
from db import session

import colorama
from colorama import Fore, Style
colorama.init()

import logging
logger = logging.getLogger("sqlalchemy")
logger.setLevel("INFO")

# 1
def select_01():
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


# 2
def select_02():

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


# 3
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


# 4
def get_average_grade_for_all():
    average_grade = session.query(func.avg(Grade.grade).label('average_grade')).scalar()
    return average_grade


# 5
def select_courses_by_teacher_id(teacher_id):
    """
    Знайти курси, які читає викладач за ID.
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


# 6
def get_students_in_group(group_id):
    students = session.query(Student).filter(Student.group_id == group_id).all()
    return students


# 7
def get_grades_for_group_subject(group_id, subject_id):
    grades = (
        session.query(Grade, Student.student_name)
        .join(Student)
        .filter(Student.group_id == group_id)
        .filter(Grade.subject_id == subject_id)
        .all()
    )
    return grades


# 8
def average_grade_by_teacher(teacher_id):
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()

    if teacher:
        average_grade = session.query(
            func.avg(Grade.grade).label('average_grade')
        ).join(Subject).filter(Subject.teacher_id == teacher_id).first()

        if average_grade:
            return teacher.teacher_name, average_grade[0]

    return None, None


# 9
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


# 10
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



if __name__ == '__main__':
# 1
    print(f"{Fore.RED + Style.BRIGHT}::: 01. Знайти 5 студентів із найбільшим середнім балом з усіх предметів{Style.RESET_ALL}")
    print(select_01())
# 2
    print(f"{Fore.RED + Style.BRIGHT}::: 02. Знайти студента із найвищим середнім балом з певного предмета{Style.RESET_ALL}")
    print(select_02())
# 3
    print(f"{Fore.RED + Style.BRIGHT}::: 03. Знайти середній бал у групах з певного предмета{Style.RESET_ALL}")
    subject_id = 2  # Предмет id=2
    average_grade_by_group = get_average_grade_by_group_for_subject(subject_id)
    print(average_grade_by_group)

# 4
    print(f"{Fore.RED + Style.BRIGHT}::: 04. Знайти середній бал на потоці (по всій таблиці оцінок){Style.RESET_ALL}")
    average_grade_all = get_average_grade_for_all()
    print("Average grade for all: ", average_grade_all)

# 5
    print(f"{Fore.RED + Style.BRIGHT}::: 05. Знайти які курси читає певний викладач{Style.RESET_ALL}")
    select_courses_by_teacher_id(1)  # ID викладача

# 6
    print(f"{Fore.RED + Style.BRIGHT}::: 06. Знайти список студентів у певній групі{Style.RESET_ALL}")
    group_id = 1  # Група id=1
    students_in_group = get_students_in_group(group_id)
    for student in students_in_group:
        print(student.student_name)


# 7
    print(f"{Fore.RED + Style.BRIGHT}::: 07. Знайти оцінки студентів у окремій групі з певного предмета{Style.RESET_ALL}")
    group_id = 1  # Група id=1
    subject_id = 2  # Предмет id=2
    grades = get_grades_for_group_subject(group_id, subject_id)
    for grade, student_name in grades:
        print(f"Student Name: {student_name}, Grade: {grade.grade}")

# 8
    print(f"{Fore.RED + Style.BRIGHT}::: 08. Знайти середній бал, який ставить певний викладач зі своїх предметів{Style.RESET_ALL}")
    teacher_id = 3  # Викладач id=3
    teacher_name, average_grade = average_grade_by_teacher(teacher_id)

    if teacher_name and average_grade:
        print(f"Teacher Name: {teacher_name}, Average Grade: {average_grade}")
    else:
        print(f"No data found for Teacher {teacher_id}")


# 9
    print(f"{Fore.RED + Style.BRIGHT}::: 09. Знайти список курсів, які відвідує певний студент{Style.RESET_ALL}")    
    student_id = 25
    student_name, student_courses = courses_attended_by_student(student_id)

    if student_name and student_courses:
        print(f"Student ID {student_id}, {student_name}, is attending the following courses:")
        for course in student_courses:
            print(course)
    else:
        print(f"No courses found for student ID: {student_id}")


# 10
    print(f"{Fore.RED + Style.BRIGHT}::: 10. Список курсів, які певному студенту читає певний викладач{Style.RESET_ALL}")
    teacher_id = 2
    student_id = 25

    teacher_name, student_name, courses_taught = courses_taught_by_teacher_to_student(teacher_id, student_id)

    if teacher_name and student_name and courses_taught:
        print(f"Teacher {teacher_name}, teaches the following courses to Student {student_name}:")
        for course in courses_taught:
            print(course)
    else:
        print(f"No courses found taught by Teacher ID {teacher_id} to Student ID {student_id}")
