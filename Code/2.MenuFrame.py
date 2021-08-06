from tkinter import*
from   PIL import ImageTk
from tkinter import ttk
import os
#=================================================MenuFrame Class=======================================================
class MenuFRame:

    def __init__(self,root):
        self.root=root
        self.root.title("Welcome To Menu")
        self.root.geometry("1300x690+20+0")
        #self.root.resizable(False, False)
        #self.root.config(bg="white")
        self.logo_icon=PhotoImage(file="i (1).png")
        # ======BG Image====
        self.bg = ImageTk.PhotoImage(file="a.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        #===========Title label=============================
        title=Label(self.root,text="Welcome To Menu ",padx=10,image=self.logo_icon,compoun=LEFT,bd=10,relief=GROOVE,font=("impact",40,),bg="#023548",fg="white",anchor="w")
        title.pack(side=TOP,fill=X  )
        #====================All Image Icon========================
        self.Guest_icon=PhotoImage(file="Student.png")
        self.Train_icon = PhotoImage(file="Train.png")
        self.Attendance_icon = PhotoImage(file="Attendance.png")
        self.Unknown_icon = PhotoImage(file="unknown.png")
        #==========================Frames===========================
        # =================================Frame1======================================
        Frame1=Frame(self.root,bd=2,relief=RIDGE)
        Frame1.place(x=150,y=130,width=400,height=270)
        self.F1_title = Label(Frame1, text="Guest Management System ", padx=10, compoun=LEFT, bd=10,relief=GROOVE, font=("impact", 10,), bg="#023548", fg="white")
        self.F1_title.pack(side=TOP,padx=10, fill=X)
        self.lbl_image1=Button(Frame1,text="Guests",image=self.Guest_icon,compound=TOP,font=("times new roman",15),command=openfGMS, cursor="hand2",fg="white",bg="#0875B7")
        self.lbl_image1.place(x=95,y=45,width=200,height=220)
        #=================================Frame2======================================
        Frame2 = Frame(self.root, bd=2, relief=RIDGE)
        Frame2.place(x=750, y=130, width=400, height=270)
        self.F2_title = Label(Frame2, text="Train your Machine", padx=10, compoun=LEFT, bd=10, relief=GROOVE,
                              font=("impact", 10,), bg="#456C04", fg="white")
        self.F2_title.pack(side=TOP, padx=10, fill=X)
        self.lbl_image2 = Button(Frame2, text="TRAIN", image=self.Train_icon, compound=TOP,
                                 font=("times new roman", 15), command=openfTYM, cursor="hand2", fg="white", bg="#0875B7")
        self.lbl_image2.place(x=95, y=45, width=200, height=220)
        # =================================Frame3======================================
        Frame3 = Frame(self.root, bd=2, relief=RIDGE)
        Frame3.place(x=150, y=420, width=400, height=270)
        self.F3_title = Label(Frame3, text="Attendance Management System ", padx=10, compoun=LEFT, bd=10, relief=GROOVE,
                              font=("impact", 10,), bg="#FF5733", fg="white")
        self.F3_title.pack(side=TOP, padx=10,  fill=X)
        self.lbl_image3 = Button(Frame3, text="Attendance", image=self.Attendance_icon, compound=TOP,
                                 font=("times new roman", 15), command=openfAMS, cursor="hand2", fg="white", bg="#0875B7")
        self.lbl_image3.place(x=95, y=45, width=200, height=220)
        # =================================Frame4======================================
        Frame4 = Frame(self.root, bd=2, relief=RIDGE)
        Frame4.place(x=750, y=420, width=400, height=270)
        self.F4_title = Label(Frame4, text="Unknown Guests DATA", padx=10, compoun=LEFT, bd=10, relief=GROOVE,
                              font=("impact", 10,), bg="#900C3F", fg="white")
        self.F4_title.pack(side=TOP, padx=10,  fill=X)
        self.lb4_image1 = Button(Frame4, text="Unknown", image=self.Unknown_icon, compound=TOP,
                                 font=("times new roman", 15), command=openfUGD, cursor="hand2",fg="white", bg="#0875B7")
        self.lb4_image1.place(x=95, y=45, width=200, height=220)
#==========================LOGOUT=============================================
        Logout_btn = Button(self.root ,command=openfLogout  , cursor="hand2", text="Logout", fg="White", bg="#d77337", font=("times new roman", 20)).place(x=1100, y=30,width=180,height=40)

#=================================================End of MenuFrame Class================================================

def openfGMS():
    cmd = 'python 3.GuestFrame.py'
    os.system(cmd)
def openfTYM():
    cmd = 'python AttendanceProject.py'
    os.system(cmd)
def openfAMS():
    cmd = 'python 4.AttendanceFrame.py'
    os.system(cmd)
def openfUGD():
    cmd = 'python 5.UnknownFrame.py'
    os.system(cmd)
def openfLogout():
    cmd = 'python 1.LoginFrame.py'
    os.system(cmd)



root=Tk()
obj=MenuFRame(root)
root.mainloop()