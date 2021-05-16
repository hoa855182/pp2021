import math
import numpy as np
import zipfile
import os
import pickle
import curses


from domain.getMark import *
from domain.Course import *
from domain.Student import *


Mark_gpa = []

dp = curses.initscr()
curses.start_color()


# ------------------------------------Student--------------------------------#
class input:
    def numberofstudent():
        dp.addstr("Enter number of student: ")
        dp.refresh()
        Nofs = int(dp.getstr().decode())
        if Nofs >= 0:
            return Nofs
        else:
            return 0

    def addstudent():
        dp.addstr("Enter StudentID:")
        dp.refresh()
        id = dp.getstr().decode()

        dp.addstr("Enter StudentName:")
        dp.refresh()
        name = dp.getstr().decode()

        dp.addstr("Enter date of brith:")
        dp.refresh()
        dob = dp.getstr().decode()
        Student(id, name, dob)


# --------------------------------------Course------------------------------#

    def numberofcourse():
        dp.refresh()
        Nofc = int(dp.getstr().decode())
        if Nofc >= 0:
            return Nofc
        else:
            return 0

    def addCourses():
        dp.addstr("Enter CourseID:")
        dp.refresh()
        cid = dp.getstr().decode()

        dp.addstr("Enter CourseName:")
        dp.refresh()
        name = dp.getstr().decode()

        dp.addstr("Enter CourseCredit:")
        dp.refresh()
        credit = float(dp.getstr().decode())
        Course(cid, name, credit)


# -------------------------------------Mark---------------------------------#

    def addmark():
        dp.addstr("-------------------Enter mark for course of each student--------------------\n")
        dp.addstr("- Enter the courseID: ")
        cid = (dp.getstr().decode())
        if cid in CoursesID:
            dp.addstr("- Enter the StudentID: ")
            id = dp.getstr().decode()
            if id in StudentID:
                dp.addstr("- Enter mark: ")
                marks = math.floor(float(dp.getstr().decode()))
            else:
                exit()
        else:
            exit()
        Mark_Student.append(marks)
        Marks(cid, id, marks)


# -------------------------------------GPA----------------------------------#
class Gpa:
    def gPa():
        markgpa = np.array([Mark_Student])
        credit = np.array([Credit])
        dp.addstr("Enter id of Student:")
        id = dp.getstr().decode()
        if id in StudentID:
            if Courses == 1:
                gpa = markgpa / credit
            else:
                for i in range(len(Courses)):
                    totalCredit = np.sum(credit)
                    totalValue = np.sum(np.multiply(markgpa, credit))
                gpa = totalValue / totalCredit
        else:
            return 0

        Mark_gpa.append(gpa)
        for m in Mark:
            dp.addstr(" [Studentid: ] %s   [Gpa: ]%s \n" % (m.s_id(), gpa))
            dp.refresh()
            break

