
import curses


Mark = []
Mark_Student = []
Mark_gpa = []

dp = curses.initscr()
curses.start_color()


class Marks:
    def __init__(self, cid, id, marks,gpa=0):
        self.cid = cid
        self.id = id
        self.marks = marks
        self.gpa=gpa
        Mark.append(self)
        Mark_Student.append(self.marks)

    def c_id(self):
        return self.cid

    def s_id(self):
        return self.id

    def get_marks(self):
        return self.marks

    def get_gpa(self):
        return self.gpa
    def set_gpa(self,gpa):
        self.gpa = gpa
