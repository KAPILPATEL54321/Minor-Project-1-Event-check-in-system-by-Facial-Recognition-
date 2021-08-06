from tkinter import*
from   PIL import ImageTk
from tkinter import messagebox
import os
from plyer import notification
class LoginFrame:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1300x690+20+0")

        self.logo_icon = PhotoImage(file="FC.png")
        self.Scan_icon = PhotoImage(file="Scan.png")

        #======BG Image====
        self.bg=ImageTk.PhotoImage(file="a.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #============================title Frame=========================================
        title = Label(self.root, text="Event check-in system by Facial Recogination", padx=10, image=self.logo_icon, compoun=LEFT, bd=10,
                      relief=GROOVE, font=("impact", 40,), bg="#154360", fg="white", anchor="w")
        title.pack(side=TOP, fill=X)
        #====== Login Frame=====
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=50,y=250,height=340,width=500 )

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        title = Label(Frame_login, text="Admin Login Area", font=("Goudy old style", 25, "bold"), fg="#d25d17", bg="white").place(x=90,
                                                                                                                   y=100)
        lbl_user=Label(Frame_login,text="Username",font=("Goudy old Style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,height=35,width=350)

        lbl_user = Label(Frame_login, text="Password", font=("Goudy old Style", 15, "bold"), fg="gray",
                         bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_login,show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=90, y=240, height=35, width=350)

        forget_btn=Button(Frame_login,command= self.forget,cursor="hand2",text="Forget_login ?", bg="White",fg="#d77337",bd=0,font=("times new roman",15 )).place(x=90,y=280)
        Login_btn = Button(self.root ,command=self.login_function  , cursor="hand2", text="Login", fg="White", bg="#d77337", font=("times new roman", 20)).place(x=200, y=570,width=180,height=40)
        Register_btn = Button(self.root, command=openfRegister, cursor="hand2", text="Register", fg="White",
                           bg="#d77337", font=("times new roman", 20)).place(x=850, y=630, width=180, height=40)


#========================================Scan Frame======================
        Frame2 = Frame(self.root, bd=2, relief=RIDGE)
        Frame2.place(x=750, y=150, width=400, height=450)
        self.F2_title = Label(Frame2, text="CLICK To SCAN FACE ", padx=10,pady=10, compoun=LEFT, bd=10, relief=GROOVE,
                              font=("impact", 15,), bg="#456C04", fg="white")
        self.F2_title.pack(side=TOP, padx=10, fill=X)
        self.lbl_image2 = Button(Frame2, text="SCAN FACE", image=self.Scan_icon, compound=TOP,
                                 font=("times new roman", 15), command=openfScan,  cursor="hand2",fg="white", bg="#0875B7")
        self.lbl_image2.place(x=20, y=80, width=350, height=350)
#======================================login Function=====================
    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get() != "123456" or self.txt_user.get() != "Kapil":
            messagebox.showerror("Error", "Invalid username/Password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.txt_user.get()}")
            openfMenu()
    def forget(self):
        notification.notify(
            title="Forget Password Notification",
            message=" Default User:-Kapil & Password:-123456",
            timeout=10
        )

def openfMenu():
    cmd = 'python 2.MenuFrame.py'
    os.system(cmd)
def openfRegister():
    cmd = 'python 3.RegistrationFrame.py'
    os.system(cmd)
def openfScan():
    cmd = 'python AttendanceProject.py'
    os.system(cmd)

root=Tk()
obj= LoginFrame(root)
root.mainloop()
