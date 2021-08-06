import cv2
import numpy as np
import face_recognition
from datetime import datetime
import os
from tkinter import *
from tkinter import messagebox
import sqlite3
from plyer import notification
#=========================================Read Image data From Guests Table=============================================
def readdata():
    conn = sqlite3.connect("Event.db")
    cursor = conn.cursor()
    m = cursor.execute(""" SELECT Name,Photo FROM guests""")
    for x in m:
        j=x[0]
        with open("Temp/{}.jpg".format(j), 'wb') as f:
            f.write(x[1])
    conn.commit()
    cursor.close()
#=========================================Path OF photo=========================
readdata()
path = 'Temp'
images = []
classNames = []
myList = os.listdir(path)


print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
#=================================findingEncodings=====================
def findEncodings( images):
    encodeList=[]
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
# ============================markAttendance=========================
def markAttendance(name):
    def add_Attendance(name,d1,t1):
        mydb = sqlite3.connect("Event.db")
        mycursor = mydb.cursor()
        print(name,d1,t1)
        mycursor.execute(""" INSERT INTO attendance (Name,Date,Time) VALUES (?,?,?)""", (name,d1,t1))
        mydb.commit()
        mydb.close()
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            print(nameList)
        if name not in nameList:
            now = datetime.now()
            date=datetime.today()
            d1=date.strftime("%b-%d-%Y")
            t1 = now.strftime('%H:%M:%S')
            f.writelines(f'\n {name},{d1},{t1}')
            add_Attendance(name,d1,t1)

          #======================Unknown user details================================================================
def Unknown(photo):
    notification.notify(
        title="Unknown Guest Found!",
        message="Unknown Guest is trying to Enter!",
        timeout=10
    )
    print(photo)
    if (photo==True):
        class GuestFrame:

            def __init__(self, root):
                self.root = root
                self.root.title("Unknown Guest")
                self.root.geometry("500x500+100+100")

                # ==========================All Variables=======================================
                self.Name_var = StringVar()
                self.Email_var = StringVar()
                self.Contact_var = StringVar()
                self.Photo_var = PhotoImage()
                with open("Temp1/Unknown Face.jpg", 'rb') as f:
                    self.Photo_var = f.read()
                # ================================================================================================

                Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
                Manage_Frame.place(x=10, y=10, width=450, height=450)

                m_title = Label(Manage_Frame, text="Unknown Guest", bg="crimson", fg="white",
                                font=("times new roman", 20, "bold"))
                m_title.grid(row=0, columnspan=2, pady=20)

                lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white",
                                 font=("times new roman", 20, "bold"))
                lbl_name.grid(row=1, column=0, pady=2, padx=20, sticky="w")

                txt_name = Entry(Manage_Frame, textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5,
                                 relief=GROOVE)
                txt_name.grid(row=1, column=1, pady=2, padx=20, sticky="w")

                lbl_Email = Label(Manage_Frame, text="Email", bg="crimson", fg="white",
                                  font=("times new roman", 20, "bold"))
                lbl_Email.grid(row=2, column=0, pady=2, padx=20, sticky="w")

                txt_Email = Entry(Manage_Frame, textvariable=self.Email_var, font=("times new roman", 15, "bold"), bd=5,
                                  relief=GROOVE)
                txt_Email.grid(row=2, column=1, pady=2, padx=20, sticky="w")
                lbl_Contact = Label(Manage_Frame, text="Contact", bg="crimson", fg="white",
                                    font=("times new roman", 20, "bold"))
                lbl_Contact.grid(row=3, column=0, pady=2, padx=20, sticky="w")

                txt_Contact = Entry(Manage_Frame, textvariable=self.Contact_var, font=("times new roman", 15, "bold"),
                                    bd=5,
                                    relief=GROOVE)
                txt_Contact.grid(row=3, column=1, pady=2, padx=20, sticky="w")

                Addbtn = Button(Manage_Frame, text="Add", width=10, command=self.add_Guests).grid(row=4, column=1,
                                                                                                  padx=10,
                                                                                                  pady=10)

            def add_Guests(self):
                if self.Name_var.get() == "" or self.Email_var.get() == "" or self.Contact_var.get() == "":
                    messagebox.showerror("Error", "All Fields are required!!!!")
                else:
                    mydb = sqlite3.connect("Event.db")
                    mycursor = mydb.cursor()
                    print(self.Name_var.get(), self.Email_var.get(), self.Contact_var.get(), self.Photo_var)
                    mycursor.execute(""" INSERT INTO unknowns (Name,Email,Contact,Photo) VALUES (?,?,?,?)""",
                                     (
                                     self.Name_var.get(), self.Email_var.get(), self.Contact_var.get(), self.Photo_var))
                    mydb.commit()
                    mydb.close()
                    messagebox.showinfo("Success", "Record has been Inserted")
                    notification.notify(
                        title="Unknown User  Found!",
                        message=" Record has been registered! ",
                        timeout=10
                    )

        root1 = Tk()
        obj = GuestFrame(root1)
        root1.mainloop()

#=================================================================
encodeListKnown = findEncodings(images)
print( 'No of Encoding Complete Done',len(encodeListKnown))
cap = cv2.VideoCapture(0)
i = 0
while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS =cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame= face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis= face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDis)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #qprint(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, "IF IT IS YOUR PHOTO THEN PRESS K ", (5,22), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, "Else press Q to quit", (5, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255),2)
            ok = cv2.waitKey(1)
            if ok  == ord("k"):
                markAttendance(name)
                cv2.putText(img, "Your Attendance Marked successfully", (5, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        else:
            name="Unknown Face"
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, "IF IT IS YOUR PHOTO THEN PRESS K ", (5, 22), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255),
                        2)
            cv2.putText(img, "Else press Q to quit", (5, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            i = i + 1
            print(i)
            if (i>=2):
                photo=cv2.imwrite("Temp1/{}.jpg".format(name), img)
                Unknown(photo)
                i=0
    key = cv2.waitKey(1)

    if key == ord("q"):
        break
    cv2.imshow('webcam',img)
cv2.destroyAllWindows()
