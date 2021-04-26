import curses
from domain import Course, Mark, Student
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


# -------------------------------------Student------------------------------#

def ListStudent():
    dp.addstr("Show lists of student:\n")
    dp.refresh()
    for s in Students:
        dp.addstr("Student id:  [%s],    Student Name:  [%s],     DOB: [%s] \n" % (
            s.s_id(), s.s_name(), s.s_dob()))
        dp.refresh()


# ------------------------------------Course--------------------------------#
def ListCourses():
    dp.addstr("Show lists of Courses:\n")
    dp.refresh()
    for c in Courses:
        dp.addstr("CourseID:  [%s],     CourseName:  [%s],     CourseCredits:  [%s] \n" % (
            c.c_id(), c.c_name(), c.c_credit()))
        dp.refresh()


# --------------------------------------Mark---------------------------------#

def ListMarks():
    dp.addstr("Show lists of mark:\n")
    dp.refresh()
    for m in Mark:
        dp.addstr("Courses id:  [%s],     Student id:  [%s]    Mark:  [%s]\n" % (
            m.c_id(), m.s_id(), m.get_marks()))
        dp.refresh()
