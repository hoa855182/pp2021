Students=[]
StudentID=[]
Courses=[]
CoursesID=[]
Mark=[]

def numberofstudent():
    Nofm = int(input("Enter the numbers of Student:"))
    if Nofm > 0:
        return Nofm
    else:
        print("There is 0 student!")
        return 0

def addStudent():
    print("ADD STUDENT FOR THIS COURSES:")
    inputs = { 'S_ID': '','Name': '','DOB': ''}
    print("Student ID:")
    inputs['S_ID'] = s_id = input()
    print("Student Name:")
    inputs['Name'] = input()
    print("date of brith:")
    inputs['DOB'] = input()
    Students.append(inputs)
    StudentID.append(s_id)

def ShowStudentInfo():
    print("StudentInfo:")
    for i in range(0,len(Students)):
        print("[Student ID:",Students[i]['S_ID'],"]","[Student name:",Students[i]['Name'],"]","[Date of Birth:",Students[i]['DOB'],"]")

def numberofcourses():
    Nofc = int(input("Enter the numbers of course:"))
    if Nofc > 0:
        return Nofc
    else:
        return 0

def addCourse():
    print("ADD COURSES:")
    input_C = {'C_ID': '', 'C_Name': '', 'Year': ''}
    print("CoursesID:")
    input_C['C_ID'] = c_id = input()
    print("CoursesName:")
    input_C['C_Name'] = input()
    print("Year:")
    input_C['Year']= input()
    Courses.append(input_C)
    CoursesID.append(c_id)

def ShowCoursesInfo():
    print("Lists of courses:")
    for i in range(0,len(Courses)):
        print("[Course ID: ",Courses[i]['C_ID'],"]","[Course name:",Courses[i]['C_Name'],"]","[Year:",Courses[i]['Year'],"]")


def mark():
    print("Enter mark for course of each student: ")
    input_M = { 'C_ID': '','S_ID': '','Mark': ''}
    print("Enter the course ID:")
    input_M['C_ID'] =idc=input()
    if idc in CoursesID:
        print("enter the student id:")
        input_M['S_ID'] = ids = input()
        if ids in StudentID:
            print("enter mark:")
            input_M['mark'] = float(input())
        else:
            return -1
    else:
        return -1
    Mark.append(input_M)

def ShowMarks():
    print("Show marks of Student in courses:")
    for i in range(len(Students)):
        print("[Course id:",Mark[i]['C_ID'],"]","[Student id:",Mark[i]['S_ID'],"]","[",Mark[i]['mark'],"]",)




def StudentManagement():
        print("ADD COURSES:")
        Nofc=numberofcourses()
        for i in range(Nofc):
            addCourse()
            Nofm=numberofstudent()
            for i in range(Nofm):
                print("1.INPUT STUDENT:")
                print("2.Stop:")
                option=int(input("YOU CHOOSE:"))
                if option==1:
                    for i in range(Nofm):
                        addStudent()
                        ShowCoursesInfo()
                        ShowStudentInfo()
                        print("1.ADD marks:")
                        print("2.Stop:")
                        option1=int(input("YOU CHOOSE:"))
                        if option1==1:
                            mark()
                            ShowCoursesInfo()
                            ShowStudentInfo()
                            ShowMarks()
                            break
                        else:
                            exit()
                else:
                    exit()
ShowMarks()
StudentManagement()
