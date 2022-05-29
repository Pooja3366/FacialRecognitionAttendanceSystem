import cx_Freeze
import sys
import os
base = None

if sys.platform =='win32':
    base == "Win32GUI"
    
os.environ['TCL_LIBRARY'] = r"C:\Users\annam\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\annam\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("Face_recognition_Software.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Face_recognition_Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll','college_images','data','database','attendance_report']}},
    version="2.0",
    description="Face Recognition Attendance Management System",
    executables=executables    
)