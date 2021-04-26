# Student management

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




#--------------------------code for manage student----------------------#
class Student:
    @staticmethod
    def numberofstudent():
        dp.addstr("Enter number of student: ")
        dp.refresh()
        Nofs = int(dp.getstr().decode())
        if Nofs >= 0:
            return Nofs
        else:
            return 0

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

    def ListStudent():
        dp.addstr("Show lists of student:\n")
        dp.refresh()
        for s in Students:
            dp.addstr("Student id:  [%s],    Student Name:  [%s],     DOB: [%s] \n" % (
            s.s_id(), s.s_name(), s.s_dob()))
            dp.refresh()

# -------------------------------------code for manage Course----------------------------------------#

class Course:

    @staticmethod
    def numberofcourse():
        dp.refresh()
        Nofc= int(dp.getstr().decode())
        if Nofc >= 0:
            return Nofc
        else:
            return 0


    def __init__(self, cid, name, credit):
        self.cid = cid
        self.name = name
        self.credit = credit
        Courses.append(self)
        CoursesID.append(self.cid)
        Credit.append(self.credit)

    def c_id(self):
        return self.cid

    def c_name(self):
        return self.name

    def c_credit(self):
        return self.credit

    @staticmethod
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

    def ListCourses():
        dp.addstr("Show lists of Courses:\n")
        dp.refresh()
        for c in Courses:
            dp.addstr("CourseID:  [%s],     CourseName:  [%s],     CourseCredits:  [%s] \n" % (
            c.c_id(), c.c_name(), c.c_credit()))
            dp.refresh()


# ----------------------------------------Mark----------------------------------------#

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

    @staticmethod
    def addmark():
        dp.addstr("-------------------Enter mark for course of each student--------------------\n")
        dp.addstr("- Enter the courseID: ")
        cid = (dp.getstr().decode())
        if cid in CoursesID:
            dp.addstr("- Enter the StudentID: ")
            id = dp.getstr().decode()
            if id in StudentID:
                dp.addstr("-Enter mark: ")
                marks = math.floor(float(dp.getstr().decode()))
            else:
                exit()
        else:
            exit()

        Marks(cid, id, marks)

    @staticmethod
    def ListMarks():
        dp.addstr("Show lists of mark:\n")
        dp.refresh()
        for m in Mark:
            dp.addstr("Courses id:  [%s],     Student id:  [%s]    Mark:  [%s]\n" % (
                m.c_id(), m.s_id(), m.get_marks()))
            dp.refresh()
class Gpa:
    def gpa():
        markgpa= np.array([Mark_Student])
        credit = np.array([Credit])
        dp.addstr("Enter id of Student:")
        id = dp.getstr().decode()
        if id in StudentID:
            if Courses == 1:
                GPA = markgpa / credit
            else:
                for i in range(len(Courses)):
                    totalCredit = np.sum(credit)
                    totalValue = np.sum(np.multiply(markgpa, credit))
                GPA = totalValue / totalCredit
        else:
            return 0

        Mark_gpa.append(GPA)
        for m in Mark:
            dp.addstr(" [Studentid: ] %s   [Gpa: ]%s \n" % (m.s_id(), GPA))
            dp.refresh()
            break
# ------------------------------------------Show--------------------------------------#

class main:


    @staticmethod
    def StudentProgrammanagement():
        dp.addstr("-------------Welcome to my program---------------\n")
        dp.refresh()
        curses.napms(3000)
        dp.clear()

        dp.addstr("-------------PLEASE ADD COURSES FRIST---------------\n")
        dp.refresh()
        curses.napms(3000)
        dp.clear()
        dp.addstr("1, Enter number of courses: \n")
        dp.addstr("2, Stop! \n")
        dp.addstr(("YOU CHOSE: "))
        option=int(dp.getstr().decode())
        if option==1:
            Nofc = Course.numberofcourse()
            dp.clear()
            dp.refresh()
            for i in range(Nofc):
                Course.addCourses()
                dp.refresh()
                dp.addstr("-------------PLEASE ADD STUDENT FOR THIS COURSE---------------\n")
                dp.refresh()
                curses.napms(2000)
                dp.clear()
                dp.addstr("1. INPUT STUDENT\n")
                dp.addstr("2. STOP!\n")
                dp.addstr("YOU CHOSE: ")
                option=int(dp.getstr().decode())
                if option==1:
                    Nofs = Student.numberofstudent()
                    dp.clear()
                    dp.refresh()
                    for i in range(Nofs):
                        Student.addstudent()
                        dp.clear()
                        dp.refresh()
                        Course.ListCourses()
                        Student.ListStudent()
                        Marks.addmark()
                        Marks.ListMarks()
                        dp.refresh()
                        dp.addstr("1. GET GPA OF STUDENT\n")
                        dp.addstr("2. STOP!\n")
                        dp.addstr("YOU CHOSE: ")
                        dp.refresh()
                        option=int(dp.getstr().decode())
                        if option==1:
                            Gpa.gpa()
                            dp.addstr("THATS ALL!")
                            curses.napms(4000)
                            dp.clear()
                            dp.addstr("DO YOU WANT TO END THE PROGRAM?\n")
                            dp.addstr("1.YES!\n")
                            dp.addstr("2.NO!\n")
                            dp.addstr("YOU CHOSE: ")
                            option = int(dp.getstr().decode())
                            if option==1:
                                dp.addstr("Good Bye!")
                                dp.refresh()
                                curses.napms(4000)
                                curses.endwin()
                                exit()
                            else:
                                dp.clear()
                                main.StudentProgrammanagement()
                                dp.refresh()
                        else:
                            dp.addstr("Good Bye!")
                            dp.refresh()
                            curses.napms(4000)
                            curses.endwin()
                            exit()
                else:
                    dp.addstr("Good Bye!")
                    dp.refresh()
                    curses.napms(4000)
                    curses.endwin()
                    exit()
        else:
            dp.addstr("Good Bye!")
            dp.refresh()
            curses.napms(4000)
            curses.endwin()
            exit()


if __name__ == '__main__':
    dp = curses.initscr()
    curses.start_color()
    main.StudentProgrammanagement()