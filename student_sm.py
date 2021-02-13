# https://www.youtube.com/watch?v=dlRXp4YSuG4&ab_channel=DJOamen
from tkinter import *
import tkinter.messagebox
#import stdDatabase
import stdDatabase_BackEnd

class Student:

    def __init__(self, root):
        self.root  = root
        self.root.title("Student Database Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="cadet blue")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()
        
        #================== FUNCTIONS =============================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Database Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
            return

        def clearData():
            self.txtStdID.delete(0, END)
            self.txtFirstname.delete(0, END)
            self.txtSurname.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtMobile.delete(0, END)
            return

        def addData():
            stdDatabase_BackEnd.studentData()
            if (len(StdID.get()) !=0):
                stdDatabase_BackEnd.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), \
                     Mobile.get())
                studentList.delete(0, END)
                studentList.insert(END, (StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), \
                     Mobile.get()))

            #stdDatabase_BackEnd
        
        def DisplayData():
            studentList.delete(0, END)
            for row in stdDatabase_BackEnd.viewData():
                studentList.insert(END, row, str(""))
        
        def StudentRec(event):
            global sd
            searchStd = studentList.curselection()[0]
            sd =  studentList.get(searchStd)

            print('\n\StudentRec FUNCTION', sd, '\n\n')

            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END, sd[1])
            self.txtFirstname.delete(0, END)
            self.txtFirstname.insert(END, sd[2])
            self.txtSurname.delete(0, END)
            self.txtSurname.insert(END, sd[3])
            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END, sd[4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[5])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[6])
            self.txtAddress.delete(0, END)
            self.txtAddress.insert(END, sd[7])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, sd[8])
        
        
        def deleteData():
            searchStd = studentList.curselection()[0]
            sd =  studentList.get(searchStd)

            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END, sd[1])
            self.txtFirstname.delete(0, END)
            self.txtFirstname.insert(END, sd[2])
            self.txtSurname.delete(0, END)
            self.txtSurname.insert(END, sd[3])
            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END, sd[4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[5])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[6])
            self.txtAddress.delete(0, END)
            self.txtAddress.insert(END, sd[7])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, sd[8])

            
            if len(StdID.get()) != 0:
                stdDatabase_BackEnd.deleteRec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            studentList.delete(0, END)
            for row in stdDatabase_BackEnd.searchData(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()):
                studentList.insert(END, row, str(""))

        def update():
            if (len(StdID.get()) !=0):
                stdDatabase_BackEnd.deleteRec(sd[0])
            if (len(StdID.get()) !=0):
                stdDatabase_BackEnd.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), \
                     Mobile.get())
                studentList.delete(0, END)
                studentList.insert(END, (StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), \
                     Mobile.get()))

        #================== FRAMES =============================================
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief =  RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTit = Label(TitleFrame, font=("arial", 47, 'bold'), text="Student Database Management Systems", bg="Ghost White")
        self.lblTit.grid()

        #---------------- LEFT and RIGHT FRAMES ----------------
        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief =  RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=2, width=1350, height=400, padx=20, pady=20, relief=RIDGE,  bg="Cadet Blue")
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1,  width=1000, height=700, padx=20, pady=8, relief=RIDGE,  bg="Ghost White",
                        font=("arial", 20, 'bold'), text="Student Information\n")
        DataFrameLeft.pack(side=LEFT)    

        DataFrameRight = LabelFrame(DataFrame, bd=1,  width=350, height=700, padx=31 , pady=3, relief=RIDGE,  bg="Ghost White",
                        font=("arial", 20, 'bold'), text="Student Details\n")
        DataFrameRight.pack(side=RIGHT)


        #================== LABELS and ENTRY WIDGETS ==========================
        self.lblStdID = Label(DataFrameLeft, font=("arial", 20, 'bold'), text="Student ID:", padx=2, pady=2, bg="Ghost White")
        self.lblStdID .grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLeft, font=("arial", 20, 'bold'), text=StdID, width=39)
        self.txtStdID .grid(row=0, column=1)

        self.lblFirstname = Label(DataFrameLeft, font=("arial", 20, 'bold'), text="First Name:", padx=2, pady=2, bg="Ghost White")
        self.lblFirstname .grid(row=1, column=0, sticky=W)
        self.txtFirstname = Entry(DataFrameLeft, font=("arial", 20, 'bold'), text=Firstname, width=39)
        self.txtFirstname .grid(row=1, column=1)
        
        self.lblSurname = Label(DataFrameLeft, font=("arial", 20, 'bold'), text="Last Name:", padx=2, pady=2, bg="Ghost White")
        self.lblSurname .grid(row=2, column=0, sticky=W)
        self.txtSurname = Entry(DataFrameLeft, font=("arial", 20, 'bold'), text=Surname, width=39)
        self.txtSurname .grid(row=2, column=1)
        
        self.lblDoB = Label(DataFrameLeft, font=("arial", 20, 'bold'), text="Date of Birth:", padx=2, pady=2, bg="Ghost White")
        self.lblDoB .grid(row=3, column=0, sticky=W)
        self.txtDoB= Entry(DataFrameLeft, font=("arial", 20, 'bold'), text=DoB, width=39)
        self.txtDoB .grid(row=3, column=1)
        
        self.lblAge = Label(DataFrameLeft, font=("arial", 20, 'bold'), text="Age:", padx=2, pady=2, bg="Ghost White")
        self.lblAge .grid(row=4, column=0, sticky=W)
        self.txtAge= Entry(DataFrameLeft, font=("arial", 20, 'bold'), text=Age, width=39)
        self.txtAge .grid(row=4, column=1)

        self.lblGender = Label(DataFrameLeft, font=("arial", 20, 'bold'), text="Gender:", padx=2, pady=2, bg="Ghost White")
        self.lblGender .grid(row=5, column=0, sticky=W)
        self.txtGender= Entry(DataFrameLeft, font=("arial", 20, 'bold'), text=Gender, width=39)
        self.txtGender .grid(row=5, column=1)

        self.lblAddress = Label(DataFrameLeft, font=("arial", 20, 'bold'), text="Address:", padx=2, pady=2, bg="Ghost White")
        self.lblAddress .grid(row=6, column=0, sticky=W)
        self.txtAddress= Entry(DataFrameLeft, font=("arial", 20, 'bold'), text=Address, width=39)
        self.txtAddress.grid(row=6, column=1)

        self.lblMobile = Label(DataFrameLeft, font=("arial", 20, 'bold'), text="Mobile:", padx=2, pady=2, bg="Ghost White")
        self.lblMobile .grid(row=7, column=0, sticky=W)
        self.txtMobile= Entry(DataFrameLeft, font=("arial", 20, 'bold'), text=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1)
        
        #================== ListBox & ScrollBar Widget ==========================
        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky="ns")

        studentList =  Listbox(DataFrameRight, width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        #studentList.bind('<<ListBoxSelect>>', StudentRec)
        studentList.bind('<Double-1>', StudentRec)
        studentList.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentList.yview)


        #================== BUTTON WIDGET ==========================
        self.btnAddDate = Button(ButtonFrame, text="Add New", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=addData)
        self.btnAddDate.grid(row=0, column=0)

        self.btnDisplay = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=DisplayData)
        self.btnDisplay.grid(row=0, column=1)

        self.btnClear = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=clearData)
        self.btnClear.grid(row=0, column=2)

        self.btnDelete = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=deleteData)
        self.btnDelete.grid(row=0, column=3)

        self.btnSearch = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=searchDatabase)
        self.btnSearch.grid(row=0, column=4)

        self.btnUpdate = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=update)
        self.btnUpdate.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)
        

        

        
        
if __name__ == "__main__":
    root =  Tk()
    application = Student(root)
    root.mainloop()