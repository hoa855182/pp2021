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
        s = open("students.txt", "w")
        s.write("Student ID: " + id + "\n" + "Student Name: " + name + "\n" +"Date of birth: " + dob + "\n")
        s.close()
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
        c = open("courses.txt", "w")
        c.write("Course id: " + cid + "\n" +"Course Name: " + name + "\n" + "Credit: " + str(credit) + "\n")
        c.close()
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
        m = open("marks.txt", "w")
        m.write("Student id: " + id + "\n"+ "Course id: " + cid + "\n" +"Mark: " + str(marks) + "\n")
        m.close()
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
            dp.addstr(" Studentid:  %s   Gpa: %s \n" % (m.s_id(), gpa))
            dp.refresh()
            break

#------------------------------------FILELIST--------------------------------#
class Filelist:
    def Createdatfile():
        filelist = ['students.txt', 'courses.txt', 'marks.txt']
        with zipfile.ZipFile('student.dat', 'w') as new_zip:
            for file in filelist:
                new_zip.write(file)
            for file in filelist:
                os.remove(file)
        dp.addstr("The Dat file is create complete!\n")

    def Extracfile():
        if os.path.isfile('student.dat'):
            zip_file = zipfile.ZipFile('student.dat', 'r')
            dp.addstr("The file is Extracting ...\n")
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
            del zip_file