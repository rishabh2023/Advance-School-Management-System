import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\sahuj\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\sahuj\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables = cx_Freeze.Executable("software.py", base=base,shortcutName='School Management',icon = 'school.ico' )

cx_Freeze.setup(
    name = "School management app",
    options = {"build_exe": {"packages":["tkinter",'os','pymysql'], "include_files":['tcl86t.dll','tk86t.dll','attendence.png','boss.png','fees.png','formnew.png','result.png','school.png','students.png','Tc.png','time-and-date.png','user.png','studentslogo.jpeg','LOGIN!.jpeg','boss.png','password.png','school.ico','Aboutus.png']}},
    version = "1.0",
    description = "Advance school management system here you will all things that is usefull in school",
    author = 'UltraCreation',
    executables = [executables],
    )
