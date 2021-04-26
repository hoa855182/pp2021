# Student management

import curses
from intput import gpa, numberofstudent, numberofcourse, addmark, addstudent, addCourses
from output import ListMarks, ListStudent, ListCourses

Students = []
StudentID = []
Courses = []
CoursesID = []
Credit = []
Mark = []
Mark_Student = []
Mark_gpa = []


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
            Nofc = numberofcourse()
            dp.clear()
            dp.refresh()
            for i in range(Nofc):
                addCourses()
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
                    Nofs = numberofstudent()
                    dp.clear()
                    dp.refresh()
                    for i in range(Nofs):
                        addstudent()
                        dp.refresh()
                        ListCourses()
                        ListStudent()
                        addmark()
                        ListMarks()
                        dp.refresh()
                        dp.addstr("1. GET GPA OF STUDENT\n")
                        dp.addstr("2. STOP!\n")
                        dp.addstr("YOU CHOSE: ")
                        dp.refresh()
                        option=int(dp.getstr().decode())
                        if option==1:
                            gpa()
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