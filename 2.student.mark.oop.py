Students = []
StudentID = []
Courses = []
CoursesID = []
Marks = []


# -------------------------------------------------student-------------------------------#
class Student:
    def __init__(self, id, name, Dob):
        self.id = id
        self.name = name
        self.Dob = Dob
        Students.append(self)
        StudentID.append(self.id)

    def information(self):
        print("Student Name:","[", self.name,"]","StudentID:","[", self.name,"]","Date of Birth:","[", self.Dob,"]")

    @staticmethod
    def numberofstudent():
        Nofm = int(input("Enter the numbers of Student:"))
        if Nofm > 0:
            return Nofm
        else:
            print("There is 0 student!")
            return 0

    @staticmethod
    def addStudent():
        print("ADD STUDENT FOR THIS COURSES:")
        print("Student ID:")
        id = input()
        print("Student Name:")
        name = input()
        print("date of brith:")
        Dob = input()
        Student(id, name, Dob)

    @staticmethod
    def ShowStudentInfo():
        print("-------------------Student Infomation-----------------")
        for i in range(0, len(Students)):
            print(Student.information(Students[i]))


# -------------------------------------course--------------------------------------#
class Course:
    def __init__(self, c_id, namec, year):
        self.c_id = c_id
        self.namec = namec
        self.year = year
        Courses.append(self)
        CoursesID.append(self.c_id)

    def InformationCoure(self):
        print("Course name:","[",self.namec,"]", "Course ID: ","[",self.c_id,"]","Year:","[",self.year,"]")

    @staticmethod
    def numberofcourses():
        Nofc = int(input("Enter the numbers of course:"))
        if Nofc > 0:
            return Nofc
        else:
            return 0

    @staticmethod
    def addCourse():
        print("CoursesID:")
        c_id = input()
        print("CoursesName:")
        namec = input()
        print("Year:")
        year = input()
        Course(c_id, namec, year)

    @staticmethod
    def ShowCoursesInfo():
        print("------------Lists of courses:------------------")
        for i in range(0, len(Courses)):
            print(Course.InformationCoure(Courses[i]))


# -------------------------mark--------------------------------#
class Mark:
    def __init__(self, c_id, id, midterm_mark,final_mark,average_mark):
        self.c_id = c_id
        self.id = id
        self.midterm_mark = midterm_mark
        self.final_mark = final_mark
        self.average_mark= average_mark
        Marks.append(self)

    def InformationMark(self):
        print("CourseID: ","[",self.c_id,"]", "StudentID:","[",self.id,"]", "Midterm Mark: ","[",self.midterm_mark,"]","Final Mark: ","[",self.final_mark,"]","Average Mark: ","[",self.average_mark,"]")

    @staticmethod
    def addmark():
        print("-------------------Enter mark for course of each student--------------------")
        print("Enter the course ID:")
        c_id = input()
        if c_id in CoursesID:
            print("Enter the student id:")
            id = input()
            if id in StudentID:
                print("Enter Midterm mark: ")
                midterm_mark = float(input())
                print("Enter Final mark: ")
                final_mark = float(input())
                average_mark = (midterm_mark + final_mark)/2
            else:
                return -1
        else:
            return -1
        Mark(c_id, id, midterm_mark,final_mark,average_mark)

    @staticmethod
    def ShowMarks():
        print("--------------Show marks of Student in courses:-----------------")
        for i in range(len(Students)):
            print(Mark.InformationMark(Marks[i]))


# --------------------------------------Start-------------------------------#

class Main:
    def StudentManagement():
        print("-------------ADD COURSES FRIST---------------")
        Nofc = Course.numberofcourses()
        for i in range(Nofc):
            Course.addCourse()
            Nofm = Student.numberofstudent()
            for i in range(Nofm):
                print("1.INPUT STUDENT:")
                print("2.Stop:")
                option = int(input("YOU CHOOSE:"))
                if option == 1:
                    for i in range(Nofm):
                        Student.addStudent()
                        Course.ShowCoursesInfo()
                        Student.ShowStudentInfo()
                        print("1.ADD marks:")
                        print("2.Stop:")
                        option1 = int(input("YOU CHOOSE:"))
                        if option1 == 1:
                            Mark.addmark()
                            Course.ShowCoursesInfo()
                            Student.ShowStudentInfo()
                            Mark.ShowMarks()
                            break
                        else:
                            exit()
                else:
                    exit()
                    Mark.ShowMarks()
    StudentManagement()
