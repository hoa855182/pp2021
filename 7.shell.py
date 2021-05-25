import os

print("Welcome to my program!")
print("This is my Working Director: ", os.getcwd())

workingdir= os.getenv("HOME")
cmd = os.chdir(workingdir)
cmd = ""

while True:
    cmd = input("hoa@hoa-Inspiron-3593:~" + os.getcwd() + "$")
    if cmd.split()[0] == "cd:":
        try:
            os.chdir(cmd[3:])
        except FileNotFoundError:
            print("bash: NO SUCH FILE OR DIRECTORY")
    elif cmd == exit():
        break
    else:
        os.system(cmd)

