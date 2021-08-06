import os
from tkinter import*
from   PIL import ImageTk
from tkinter import ttk
from tkinter import  messagebox

from tkinter import filedialog,messagebox
import sqlite3
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1300x650+25+25")
        self.root.resizable(False,False)
        #======BG Image====
        self.bg=ImageTk.PhotoImage(file="a.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #====== Login Frame=====
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=50,y=150,height=340,width=500 )

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        title = Label(Frame_login, text="Admin Login Area", font=("Goudy old style", 25, "bold"), fg="#d25d17", bg="white").place(x=90,
                                                                                                                   y=100)
        lbl_user=Label(Frame_login,text="Username",font=("Goudy old Style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,height=35,width=350)

        lbl_user = Label(Frame_login, text="Password", font=("Goudy old Style", 15, "bold"), fg="gray",
                         bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=90, y=240, height=35, width=350)

        forget_btn=Button(Frame_login,cursor="hand2",text="Forget_login ?", bg="White",fg="#d77337",bd=0,font=("times new roman",15 )).place(x=90,y=280)
        Login_btn = Button(self.root ,command=self.login_function  , cursor="hand2", text="Login", fg="White", bg="#d77337", font=("times new roman", 20)).place(x=200, y=470,width=180,height=40)

    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get() != "123456" or self.txt_user.get() != "Kapil":
            messagebox.showerror("Error", "Invalid username/Password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.txt_user.get()}")
            call_main()

        print("YOUR name:= ",self.txt_user.get())

class GuestFrame:

    def __init__(self,root):
        self.root=root
        self.root.title("Guests Management System")
        self.root.geometry("1300x690+20+0")

        # ======BG Image===========================================
        self.bg = ImageTk.PhotoImage(file="a.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        #===========Title label=====================================
        title=Label(self.root,text="Guests Management System ",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#3A5B04",fg="white")
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


#======================Manage Left Frame =================================

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="Manage Guests",bg="crimson",fg="white",font=("times new roman",20,"bold"))
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

        Addbtn=Button(btn_Frame,text="Add",width=10 ,command=self.add_Guests).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn = Button(btn_Frame,command=self.update_data, text="Update", width=10).grid(row=0,column=1, padx=10, pady=10)
        Deletebtn = Button(btn_Frame,command= self.delete_data,text="Delete", width=10).grid(row=0,column=2 ,padx=10, pady=10)
        Clearbtn = Button(btn_Frame,command=self.clear ,text="Clear", width=10).grid(row=0,column=3, padx=10, pady=10)
# ======================Detail Frame =================================
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=800, height=580)
        lbl_search = Label(Detail_Frame, text="Search BY", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,  font=("times new roman", 13, "bold"), state="readonly")
        combo_search['values'] = ("Guest_No", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(Detail_Frame,textvariable=self.search_txt,width=15, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchallbtn = Button(Detail_Frame,command=self.search_data, text="Search", width=10,pady=5).grid(row=0, column=3, padx=10, pady=10)
        Showallbtn = Button(Detail_Frame,command=self.fetch_data ,text="ShowAll", width=10,pady=5).grid(row=0, column=4 , padx=10, pady=10)
#================================= Table Frame===========================
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=7, y=60, width=780, height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Guest_table=ttk.Treeview(Table_Frame,columns=("Guest","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Guest_table.xview)
        scroll_y.config(command=self.Guest_table.yview)
        self.Guest_table.heading("Guest",text="Guest No.")
        self.Guest_table.heading("Name",text="Name")
        self.Guest_table.heading("Email",text="Email")
        self.Guest_table.heading("Gender",text="Gender")
        self.Guest_table.heading("Contact",text="Contact")
        self.Guest_table.heading("DOB",text="DOB")
        self.Guest_table.heading("Address",text="Address")
        self.Guest_table['show']='headings'
        self.Guest_table.column("Guest",width=100)
        self.Guest_table.column("Name", width=150)
        self.Guest_table.column("Gender", width=100)
        self.Guest_table.column("Contact", width=150)
        self.Guest_table.column("DOB", width=100)
        self.Guest_table.column("Address", width=250)

        self.Guest_table.pack(fill=BOTH,expand=1)
        self.Guest_table.bind("<ButtonRelease-1>",self.get_cursor )
        self.fetch_data()

    def savedata(self):
        fn = filedialog.askopenfilename(title="Select File", filetypes=(("Image File", "*.jpg"), ("All Files", "*.*")))
        with open(fn, "rb") as f:
            self.Photo_var= f.read()  # this is our binary data
    def add_Guests(self):
        if self.Guest_No_var.get()=="" or self.Name_var.get()=="" or self.Email_var.get()=="" or self.Contact_var.get()=="" or self.DOB_var.get()=="" or self.Gender_var.get()=="" or self.txt_Address.get('1.0',END)=="":
            messagebox.showerror("Error","All Fields are required!!!!")
        else:
            mydb = sqlite3.connect("Guests.db")
            mycursor = mydb.cursor()
            #mydb = mysql.connector.connect(host="localhost", user="root", password="Kapil@123",database="stm")
            #mycursor = mydb.cursor()
            print(self.Guest_No_var.get(), self.Name_var.get(), self.Email_var.get(), self.Gender_var.get(),
                  self.Contact_var.get(), self.DOB_var.get(), self.txt_Address.get('1.0', END))
            #mycursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.Guest_No_var.get(),self.Name_var.get(),self.Email_var.get(),self.Gender_var.get(),self.Contact_var.get(),self.DOB_var.get(),self.txt_Address.get('1.0',END),self.Photo_var))
            mycursor.execute(""" INSERT INTO students (Guest_No,Name,Email,Gender,Contact,DOB,Address,Photo) VALUES (?,?,?,?,?,?,?,?)""", (self.Guest_No_var.get(),self.Name_var.get(),self.Email_var.get(),self.Gender_var.get(),self.Contact_var.get(),self.DOB_var.get(),self.txt_Address.get('1.0',END),self.Photo_var))
            mydb.commit()
            self.fetch_data()
            self.clear()
            mydb.close()
            messagebox.showinfo("Success","Record has been Inserted")
    def fetch_data(self):
        mydb = sqlite3.connect("students.db")
        mycursor = mydb.cursor()
        mycursor.execute("Select * from students")
        rows=mycursor.fetchall()
        print(rows)
        if len(rows)!=0:
                self.Guest_table.delete(*self.Guest_table.get_children())
                for row in rows:
                        self.Guest_table.insert("",END,values=row)
                mydb.commit()
        mydb.close()
    def clear(self):
        self.Guest_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.DOB_var.set("")
        self.txt_Address.delete("1.0",END)

    def get_cursor(self,ev):
        curosor_row=self.Guest_table.focus()
        contents=self.Guest_table.item(curosor_row)
        row=contents["values"]
        self.Guest_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[6])

    def update_data(self):
        mydb = sqlite3.connect("students.db")
        mycursor = mydb.cursor()
        print(self.Guest_No_var.get(), self.Name_var.get(), self.Email_var.get(), self.Gender_var.get(),
              self.Contact_var.get(), self.DOB_var.get(), self.txt_Address.get('1.0', END),self.Photo_var)
        mycursor.execute(
            """ update students set Name=?,Email=?,Gender=?,Contact=?,DOB=?,Address=?,Photo=? where Guest_No=?""",
            ( self.Name_var.get(), self.Email_var.get(), self.Gender_var.get(),
             self.Contact_var.get(), self.DOB_var.get(), self.txt_Address.get('1.0', END), self.Photo_var,self.Guest_No_var.get()))
        mydb.commit()
        self.fetch_data()
        self.clear()
        mydb.close()
    def delete_data(self):
        mydb = sqlite3.connect("Guests.db")
        mycursor = mydb.cursor()
        mycursor.execute("delete from Guests where Guest_No=%s"%self.Guest_No_var.get())
        mydb.commit()
        mydb.close()
        self.fetch_data()
        self.clear()
    def search_data(self):
        mydb = sqlite3.connect("students.db")
        mycursor = mydb.cursor()
        mycursor.execute("Select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=mycursor.fetchall()
        if len(rows)!=0:
                self.Guest_table.delete(*self.Guest_table.get_children())
                for row in rows:
                        self.Guest_table.insert("",END,values=row)
                mydb.commit()
        mydb.close()


root=Tk()


obj= Login(root)
def call_main():
    obj = GuestFrame(root)
root.mainloop()
