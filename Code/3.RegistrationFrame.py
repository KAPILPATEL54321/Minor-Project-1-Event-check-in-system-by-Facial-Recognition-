from tkinter import*
from   PIL import ImageTk
from tkinter import ttk
from tkinter import filedialog,messagebox
import sqlite3
import os
# =================================================RegisterFrame Class==================================================
class RegisterFrame:

    def __init__(self,root):
        self.root=root
        self.root.title("Guests Registration System")
        self.root.geometry("1300x690+20+0")

        # ======BG Image===========================================
        self.bg = ImageTk.PhotoImage(file="a.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        #===========Title label=====================================
        title=Label(self.root,text="Guests Registration System ",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#3A5B04",fg="white")
        title.pack(side=TOP,fill=X  )

#==========================All Variables=======================================
        self.Guest_No_var=StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.DOB_var = StringVar()
        self.Photo_var=PhotoImage()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        Main_btn = Button(self.root, command=openfMenu, cursor="hand2", text="Home", fg="White", bg="#d77337",
                            font=("times new roman", 20)).place(x=1100, y=30, width=180, height=40)
#======================Manage Left Frame =================================

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=300,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="Register Guest",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_Guest=Label(Manage_Frame,text="Guest No",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Guest.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Guest = Entry(Manage_Frame, textvariable=self.Guest_No_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Guest.grid(row=1, column=1, pady=2, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=2, padx=20, sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.Name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=2,padx=20,sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=2, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame, textvariable=self.Email_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=2, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=2, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman", 13, "bold"), state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4, column=1, pady=2, padx=20, sticky="w")

        lbl_Contact = Label(Manage_Frame, text="Contact", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=2, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame,textvariable=self.Contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=2, padx=20, sticky="w")

        lbl_dob = Label(Manage_Frame, text="D.O.B", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=2, padx=20, sticky="w")

        txt_dob = Entry(Manage_Frame,textvariable=self.DOB_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=2, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=2, padx=20, sticky="w")

        self.txt_Address= Text(Manage_Frame, width= 30,height=4,font=("",10))
        self.txt_Address.grid(row=7, column=1, pady=2, padx=20, sticky="w")

        lbl_photo = Label(Manage_Frame, text="ADD Photo", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_photo.grid(row=8, column=0, pady=2, padx=20, sticky="w")

        upload_btn= Button(Manage_Frame, command=self.savedata, cursor="hand2", text="Upload", fg="White",
                           bg="#d77337", font=("times new roman", 20))
        upload_btn.grid(row=8, column=1, pady=20, padx=20, sticky="w")

#======================Button Frame=====================================
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=15, y=500, width=420)

        Addbtn=Button(btn_Frame,text="Add",width=10 ,command=self.add_Guests).grid(row=0,column=2,padx=60,pady=10)
        Clearbtn = Button(btn_Frame,command=self.clear ,text="Clear", width=10).grid(row=0,column=4, padx=60, pady=10)


    def savedata(self):
        fn = filedialog.askopenfilename(title="Select File", filetypes=(("Image File", "*.jpg"), ("All Files", "*.*")))
        with open(fn, "rb") as f:
            self.Photo_var= f.read()  # this is our binary data
    def add_Guests(self):
        if self.Guest_No_var.get()=="" or self.Name_var.get()=="" or self.Email_var.get()=="" or self.Contact_var.get()=="" or self.DOB_var.get()=="" or self.Gender_var.get()=="" or self.txt_Address.get('1.0',END)=="":
            messagebox.showerror("Error","All Fields are required!!!!")
        else:
            mydb = sqlite3.connect("Event.db")
            mycursor = mydb.cursor()
            #mydb = mysql.connector.connect(host="localhost", user="root", password="Kapil@123",database="stm")
            #mycursor = mydb.cursor()
            print(self.Guest_No_var.get(), self.Name_var.get(), self.Email_var.get(), self.Gender_var.get(),
                  self.Contact_var.get(), self.DOB_var.get(), self.txt_Address.get('1.0', END))
            #mycursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.Guest_No_var.get(),self.Name_var.get(),self.Email_var.get(),self.Gender_var.get(),self.Contact_var.get(),self.DOB_var.get(),self.txt_Address.get('1.0',END),self.Photo_var))
            mycursor.execute(""" INSERT INTO guests (Guest_No,Name,Email,Gender,Contact,DOB,Address,Photo) VALUES (?,?,?,?,?,?,?,?)""", (self.Guest_No_var.get(),self.Name_var.get(),self.Email_var.get(),self.Gender_var.get(),self.Contact_var.get(),self.DOB_var.get(),self.txt_Address.get('1.0',END),self.Photo_var))
            mydb.commit()

            self.clear()
            mydb.close()
            messagebox.showinfo("Success","Record has been Inserted")
    def clear(self):
        self.Guest_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.DOB_var.set("")
        self.txt_Address.delete("1.0",END)
# =================================================End of RegisterFrame Class===============================================
def openfMenu():
    cmd = 'python 2.MenuFrame.py'
    os.system(cmd)
root1=Tk()
obj=RegisterFrame(root1)
root1.mainloop()