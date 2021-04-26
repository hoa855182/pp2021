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


class Marks:
    def __init__(self, cid, id, marks, ):
        self.cid = cid
        self.id = id
        self.marks = marks
        Mark.append(self)
        Mark_Student.append(self.marks)

    def c_id(self):
        return self.cid

    def s_id(self):
        return self.id

    def get_marks(self):
        return self.marks
