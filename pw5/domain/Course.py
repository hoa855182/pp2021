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


# -------------------------------------Course---------------------------#
class Course:

    def __init__(self, cid, name, credit):
        self.cid = cid
        self.name = name
        self.credit = credit
        Courses.append(self)
        CoursesID.append(self.cid)

    def c_id(self):
        return self.cid

    def c_name(self):
        return self.name

    def c_credit(self):
        return self.credit