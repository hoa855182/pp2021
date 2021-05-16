
import pickle
import os
import curses

from domain.Course import *
from domain.Student import *
from domain.getMark import *
from intput import input,Gpa
from output import outputs

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
        dp.addstr(("YOU CHOSE:"))
        option = int(dp.getstr().decode())
        if option == 1:
            Nofc = input.numberofcourse()
            dp.clear()
            dp.refresh()
            for i in range(Nofc):
                input.addCourses()
                dp.refresh()
                dp.addstr("-------------PLEASE ADD STUDENT FOR THIS COURSE---------------\n")
                dp.refresh()
                curses.napms(2000)
                dp.clear()
                dp.addstr("1. INPUT STUDENT\n")
                dp.addstr("2. STOP!\n")
                dp.addstr("YOU CHOSE: ")
                option = int(dp.getstr().decode())
                if option == 1:
                    Nofs = input.numberofstudent()
                    dp.clear()
                    dp.refresh()
                    for i in range(Nofs):
                        input.addstudent()
                        dp.refresh()
                        input.addmark()
                        dp.refresh()
                else:
                    dp.addstr("-------------------------------Good Bye!---------------------------")
                    dp.refresh()
                    curses.napms(4000)
                    curses.endwin()
                    exit()
                break
        else:
            dp.addstr("-------------------------------Good Bye!------------------------------------")
            dp.refresh()
            curses.napms(4000)
            curses.endwin()
            dp.refresh()
            exit()
        while True:
            dp.addstr("1. Show Student :\n")
            dp.addstr("2. Show Courses :\n")
            dp.addstr("3. Show Marks :\n")
            dp.addstr("4. Calculate and Show GPA:\n")
            dp.addstr("5. Save file with pickle \n")
            dp.addstr("6. Stop\n")
            dp.addstr("You choose:  ")
            option1 = int(dp.getstr().decode())
            dp.refresh()
            dp.clear()
            dp.refresh()
            if option1 == 1:
                outputs.ListStudent()
                dp.refresh()
            if option1 == 2:
                outputs.ListCourses()
                dp.refresh()
            if option1 == 3:
                outputs.ListMarks()
                dp.refresh()
            if option1 == 4:
                Gpa.gPa()
                curses.napms(3000)
                dp.clear()
            if option1 == 5:
                if os.path.isfile('student.dat'):
                    with open('student.dat', 'w') as zipF:
                        for STUDENT in Students:
                            pickle.dump(STUDENT, zipF)
                        for COURSE in Courses:
                            pickle.dump(COURSE, zipF)
                        for MARK in Mark:
                            pickle.dump(MARK, zipF)
                        dp.refresh()
            elif option1 == 6:
                dp.addstr("-------------------------------Good Bye!---------------------------")
                dp.refresh()
                curses.napms(4000)
                curses.endwin()
                exit()



if __name__ == '__main__':
    dp = curses.initscr()
    curses.start_color()
    main.StudentProgrammanagement()