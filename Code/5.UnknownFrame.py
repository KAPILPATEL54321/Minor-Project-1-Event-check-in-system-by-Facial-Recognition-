from tkinter import*
from   PIL import ImageTk
from tkinter import ttk
import sqlite3
import os
# ================================================UnknownFrame Class===============================================
class UnknownFrame:

    def __init__(self,root):
        self.root=root
        self.root.title(" Guests Unknown Management System")
        self.root.geometry("1300x690+20+0")

        # ======BG Image===========================================
        self.bg = ImageTk.PhotoImage(file="a.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        #===========Title label=====================================
        title=Label(self.root,text="Unknown Guests  Management System ",bd=10,relief=GROOVE,font=("Contacts new roman",40,"bold"),bg="#3A5B04",fg="white")
        title.pack(side=TOP,fill=X  )

#==========================All Variables=======================================
        self.Serial_No_var=StringVar()
        self.Name_var = StringVar()
        self.Email_var= StringVar()
        self.Contact_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.Photo_var = PhotoImage()
        Menu_btn = Button(self.root, command=openfMenu, cursor="hand2", text="Menu", fg="White", bg="#d77337",
                          font=("times new roman", 20)).place(x=1150, y=30, width=130, height=40)

#======================Manage Left Frame =================================

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="Manage Unknown Detail",bg="crimson",fg="white",font=("Contacts new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_serial=Label(Manage_Frame,text="Serial No.",bg="crimson",fg="white",font=("Contacts new roman",20,"bold"))
        lbl_serial.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_serial = Entry(Manage_Frame, textvariable=self.Serial_No_var,font=("Contacts new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_serial.grid(row=1, column=1, pady=2, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white", font=("Contacts new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=2, padx=20, sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.Name_var,font=("Contacts new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=2,padx=20,sticky="w")

        lbl_Day = Label(Manage_Frame, text="Email", bg="crimson", fg="white", font=("Contacts new roman", 20, "bold"))
        lbl_Day.grid(row=3, column=0, pady=2, padx=20, sticky="w")

        txt_Day = Entry(Manage_Frame, textvariable=self.Email_var,font=("Contacts new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Day.grid(row=3, column=1, pady=2, padx=20, sticky="w")

        lbl_Contact = Label(Manage_Frame, text="Contact", bg="crimson", fg="white", font=("Contacts new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=2, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame,textvariable=self.Contact_var, font=("Contacts new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=2, padx=20, sticky="w")
        # =================================Frame3======================================
        #lbl_Photo = Label(Manage_Frame, text="Unknown", bg="crimson", fg="white",
        #                    font=("Contacts new roman", 20, "bold"))
        #lbl_Photo.grid(row=6, column=0, pady=2, padx=20, sticky="w")
        #self.lbl_image = Button(Manage_Frame, text="Unknown",  compound=TOP,
        #                         font=("times new roman", 15), command=True, cursor="hand2", fg="white", bg="#0875B7")
        #self.lbl_image.place(x=200, y=270, width=200, height=220)

#======================Button Frame=====================================
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=15, y=500, width=420)


        Updatebtn = Button(btn_Frame,command=self.update_data, text="Update", width=10).grid(row=0,column=1, padx=25, pady=10)
        Deletebtn = Button(btn_Frame,command= self.delete_data,text="Delete", width=10).grid(row=0,column=2 ,padx=25, pady=10)
        Clearbtn = Button(btn_Frame,command=self.clear ,text="Clear", width=10).grid(row=0,column=3, padx=25, pady=10)
# ======================Detail Frame =================================
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=800, height=580)
        lbl_search = Label(Detail_Frame, text="Search BY", bg="crimson", fg="white", font=("Contacts new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,  font=("Contacts new roman", 13, "bold"), state="readonly")
        combo_search['values'] = ("Name", "Email", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(Detail_Frame,textvariable=self.search_txt,width=15, font=("Contacts new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchallbtn = Button(Detail_Frame,command=self.search_data, text="Search", width=10,pady=5).grid(row=0, column=3, padx=10, pady=10)
        Showallbtn = Button(Detail_Frame,command=self.fetch_data ,text="ShowAll", width=10,pady=5).grid(row=0, column=4 , padx=10, pady=10)
#================================= Table Frame===========================
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=7, y=60, width=780, height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Guest_table=ttk.Treeview(Table_Frame,columns=("Serial No.","Name","Email","Contact"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Guest_table.xview)
        scroll_y.config(command=self.Guest_table.yview)
        self.Guest_table.heading("Serial No.",text="Serial No.")
        self.Guest_table.heading("Name",text="Name")
        self.Guest_table.heading("Email",text="Email")
        self.Guest_table.heading("Contact",text="Contact")
        self.Guest_table['show']='headings'
        self.Guest_table.column("Serial No.",width=100)
        self.Guest_table.column("Name", width=150)
        self.Guest_table.column("Email", width=100)
        self.Guest_table.column("Contact", width=150)

        self.Guest_table.pack(fill=BOTH,expand=1)
        self.Guest_table.bind("<ButtonRelease-1>",self.get_cursor )
        self.fetch_data()


    def fetch_data(self):
        mydb = sqlite3.connect("Event.db")
        mycursor = mydb.cursor()
        mycursor.execute("Select * from unknowns")
        rows=mycursor.fetchall()
        print(rows)
        if len(rows)!=0:
                self.Guest_table.delete(*self.Guest_table.get_children())
                for row in rows:
                        self.Guest_table.insert("",END,values=row)
                mydb.commit()
        mydb.close()
    def clear(self):
        self.Serial_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Contact_var.set("")
        self.Photo_var.set("")
    def get_cursor(self,ev):
        curosor_row=self.Guest_table.focus()
        contents=self.Guest_table.item(curosor_row)
        row=contents["values"]
        self.Serial_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Contact_var.set(row[3])

    def update_data(self):
        mydb = sqlite3.connect("Event.db")
        mycursor = mydb.cursor()
        print(self.Serial_No_var.get(), self.Name_var.get(), self.Email_var.get(), self.Contact_var.get())
        mycursor.execute(
            """ update unknowns set Name=?,Email=?,Contact=? where Serial_No=?""",
            ( self.Name_var.get(), self.Email_var.get(), self.Contact_var.get(),self.Serial_No_var.get()))
        mydb.commit()
        self.fetch_data()
        self.clear()
        mydb.close()
    def delete_data(self):
        mydb = sqlite3.connect("Event.db")
        mycursor = mydb.cursor()
        mycursor.execute("delete from unknowns where Serial_No=%s"%self.Serial_No_var.get())
        mydb.commit()
        mydb.close()
        self.fetch_data()
        self.clear()
    def search_data(self):
        mydb = sqlite3.connect("unknowns.db")
        mycursor = mydb.cursor()
        mycursor.execute("Select * from unknowns where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=mycursor.fetchall()
        if len(rows)!=0:
                self.Guest_table.delete(*self.Guest_table.get_children())
                for row in rows:
                        self.Guest_table.insert("",END,values=row)
                mydb.commit()
        mydb.close()
# =================================================End of UnknownFrame Class===============================================
def openfMenu():
    cmd = 'python 2.MenuFrame.py'
    os.system(cmd)
root=Tk()
obj=UnknownFrame(root)
root.mainloop()