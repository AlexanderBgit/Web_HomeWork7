from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy import select
from datetime import datetime


# import sys
# import os

# project_root = os.path.dirname(os.path.abspath(__file__))
# src_path = os.path.join(project_root, 'src')
# sys.path.append(src_path)
from db import session
# from src.db import session #глючить

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    student_name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group")


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    teacher_name = Column(String)


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    subject_name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher")


class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)


session.close()

