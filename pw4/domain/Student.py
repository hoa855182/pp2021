import math
import numpy as np
import curses
Students = []
StudentID = []

Courses = []
CoursesID = []
Credit = []

Mark = []
Mark_Student = []
Mark_gpa = []

dp = curses.initscr()
curses.start_color()


class Student:

    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        Students.append(self)
        StudentID.append(self.id)

    def s_id(self):
        return self.id

    def s_name(self):
        return self.name

    def s_dob(self):
        return self.dob
