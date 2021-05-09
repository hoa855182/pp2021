import math
import numpy as np
import zipfile
import os
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
#------------------------------------FILELIST--------------------------------#
    def file_list():
        dp.addstr("WHAT YOU WANT TO DO NEXT?\n")
        dp.addstr("1.CREATE DAT FILE\n")
        dp.addstr("2.EXTRACT THE PROGRAM!\n")
        dp.addstr("YOU CHOSE: ")
        dp.refresh()
        option = int(dp.getstr().decode())
        if option == 1:
            filelist = ['students.txt', 'courses.txt', 'marks.txt']
            with zipfile.ZipFile('student.dat', 'w') as new_zip:
                for file_name in filelist:
                    new_zip.write(file_name)
                for file_name in filelist:
                    os.remove(file_name)
        if option == 2:
            if os.path.isfile('student.dat'):
                dp.addstr("file exist\n")
                zip_file = zipfile.ZipFile('student.dat', 'r')
                dp.addstr("Extracting all the files now...\n")
                zip_file.extractall()
                if os.path.isfile('students.txt'):
                    fs = open('students.txt', 'r')
                    fs.read().splitlines()
                if os.path.isfile('courses.txt'):
                    fc = open('courses.txt', 'r')
                    fc.read().splitlines()
                if os.path.isfile('marks.txt'):
                    mf = open('marks.txt', 'r')
                    mf.read().splitlines()
        else:
            dp.addstr("Good Bye!")
            dp.refresh()
            curses.napms(4000)
            curses.endwin()
            exit()