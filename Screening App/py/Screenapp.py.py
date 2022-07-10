import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
from time import strftime
import pandas as pd

class App(Tk):
    def home(self): #fill up form for customer and widgets
       self.root =root
       canvas1 = tk.Canvas(root, width=600, height=600, relief='raised')
       canvas1.pack()

       label1 = tk.Label(root, text='Customer Registration Form')
       label1.config(font=('helvetica', 14))
       canvas1.create_window(300, 25, window=label1)

       label2 = tk.Label(root, text='Full Name:')
       label2.config(font=('helvetica', 10))
       canvas1.create_window(50, 100, window=label2)

       label3 = tk.Label(root, text='Age:')
       label3.config(font=('helvetica', 10))
       canvas1.create_window(50, 140, window=label3)

       label4 = tk.Label(root, text='Sex:')
       label4.config(font=('helvetica', 10))
       canvas1.create_window(50, 180, window=label4)

       label5 = tk.Label(root, text='Address:')
       label5.config(font=('helvetica', 10))
       canvas1.create_window(300, 140, window=label5)

       label6 = tk.Label(root, text='Cellphone no.:')
       label6.config(font=('helvetica', 10))
       canvas1.create_window(300, 180, window=label6)

       label12 = tk.Label(root, text='Answer Yes or No:')
       label12.config(font=('helvetica', 10))
       canvas1.create_window(70, 230, window=label12)

       label7 = tk.Label(root, text='Have you traveled outside of the country in the past 14 days?')
       label7.config(font=('helvetica', 10))
       canvas1.create_window(200, 280, window=label7)

       label8 = tk.Label(root,text='In the past 14 days, have you been in contact with someone who ')
       label8.config(font=('helvetica', 10))
       canvas1.create_window(213, 320, window=label8)

       label10 = tk.Label(root,
                         text='tested positive (or is currently being tested) for COVID-19?')
       label10.config(font=('helvetica', 10))
       canvas1.create_window(210, 340, window=label10)

       label9 = tk.Label(root,text='In thepast 14 days, have you been in contact with someone ')
       label9.config(font=('helvetica', 10))
       canvas1.create_window(195, 380, window=label9)

       label11 = tk.Label(root,
                         text='who exhibited any symptoms related to COVID-19)?')
       label11.config(font=('helvetica', 10))
       canvas1.create_window(190, 400, window=label11)

       self.entry1 = tk.Entry(root)
       canvas1.create_window(280, 100, window=self.entry1, width = 360)

       self.entry2 = tk.Entry(root)
       canvas1.create_window(150, 140, window=self.entry2, width = 100)

       self.entry3 = tk.Entry(root)
       canvas1.create_window(150, 180, window=self.entry3,width = 100)

       self.entry4 = tk.Entry(root)
       canvas1.create_window(450, 140, window=self.entry4,width = 200)

       self.entry5 = tk.Entry(root)
       canvas1.create_window(450, 180, window=self.entry5,width = 200)

       self.entry6 = tk.Entry(root)
       canvas1.create_window(470, 280, window=self.entry6, width=100)
       self.entry7 = tk.Entry(root)
       canvas1.create_window(470, 330, window=self.entry7, width=100)
       self.entry8 = tk.Entry(root)
       canvas1.create_window(470, 390, window=self.entry8, width=100)

       button1 = tk.Button(text='ADMIN', command=self.adminLogin, bg='white', fg='black', width=20,font=('helvetica', 9, 'bold'))
       canvas1.create_window(300, 570, window=button1)

       button2 = tk.Button(text='Submit', command = self.doneCommand,  bg='brown', fg='white', width=30,font=('helvetica', 9, 'bold'))
       canvas1.create_window(300, 490, window=button2)

       button3 = tk.Button(text='Clear All', command=self.clearBox, bg='brown', fg='white', width=30,font=('helvetica', 9, 'bold'))
       canvas1.create_window(300, 520, window=button3)

    def doneCommand(self): # calling popup and input data(to store the information to the database)
       self.popupmsg()

    def adminLogin(self): #Admin login then admin windows for configuration of data
       global root2

       try: #for window of admin
          if root2.state() == "normal": root2.focus()
       except:
           root2=tk.Toplevel()
           canvas2 = tk.Canvas(root2, width=400, height=600, relief='raised')
           canvas2.pack()
           root2.resizable(False,False)
           label1 = tk.Label(root2, text='ADMIN LOGIN')
           label1.config(font=('helvetica', 14))
           canvas2.create_window(200, 25, window=label1)

           label2 = tk.Label(root2, text='USERNAME:')
           label2.config(font=('helvetica', 10))
           canvas2.create_window(90, 100, window=label2)

           label3 = tk.Label(root2, text='PASSWORD:')
           label3.config(font=('helvetica', 10))
           canvas2.create_window(90, 140, window=label3)

           label4 = tk.Label(root2, text='Input a username and password to login.')
           label4.config(font=('helvetica', 10))
           canvas2.create_window(200, 70, window=label4)

           entry1 = tk.Entry(root2)
           canvas2.create_window(250, 100, window=entry1)

           entry2 = tk.Entry(root2)
           canvas2.create_window(250, 140, window=entry2)

           button = tk.Button(root2,text='Submit',command=lambda: self.admin(), bg='brown', fg='white', width=30,font=('helvetica', 9, 'bold'))
           canvas2.create_window(200, 200, window=button)

           button1 = tk.Button(root2, text='Back', command=root2.destroy, bg='white', fg='black', width=30,font=('helvetica', 9, 'bold'))
           canvas2.create_window(200, 240, window=button1)

    def admin(self): #destroy the adminlogin after login in the adminInterface
        self.adminInterface()
        root2.destroy()

    def popupmsg(self):  # popup message for completing the fill up form with information in it
       text1 = self.entry1.get()
       text2 = self.entry2.get()
       text3 = self.entry3.get()
       text4 = self.entry4.get()
       text5 = self.entry5.get()
       popup = tk.Tk()
       popup.wm_title("Notification!")
       label = tk.Label(popup, text='Fill-up form Complete / ' + date + " / " + time, font='tahoma')
       label.pack()
       label2 = tk.Label(popup, text=text1, font='tahoma')
       label2.pack()
       label3 = tk.Label(popup, text=text2, font='tahoma')
       label3.pack()
       label4 = tk.Label(popup, text=text3, font='tahoma')
       label4.pack()
       label5 = tk.Label(popup, text=text4, font='tahoma')
       label5.pack()
       label6 = tk.Label(popup, text=text5, font='tahoma')
       label6.pack()
       button = tk.Button(popup, text="SUBMIT", width=20, bg='brown', fg='white', command=self.inputData())
       button.pack()
       button1 = tk.Button(popup, text="Back", width=20, bg='brown', fg='white', command=popup.destroy)
       button1.pack()
       popup.geometry('400x250')
       popup.resizable(False, False)
       popup.mainloop()

    def clearBox(self):  # this will clear all the entryboxes in the fillup form for customer
       self.entry1.delete(0, 'end')
       self.entry2.delete(0, 'end')
       self.entry3.delete(0, 'end')
       self.entry4.delete(0, 'end')
       self.entry5.delete(0, 'end')
       self.entry6.delete(0, 'end')
       self.entry7.delete(0, 'end')
       self.entry8.delete(0, 'end')


    def adminInterface(self):

       global root3

       try: #for window of admin
           if root3.state() == "normal": root3.focus()
       except:
           root3=tk.Toplevel()
           canvas3 = tk.Canvas(root3, width=600, height=600, relief='raised')
           canvas3.pack()
           root3.resizable(False,False)

           frame1 = tk.LabelFrame(root3, text="Customer Data")
           frame1.place(height=250, width=550,rely=0, relx=0.05)

           file_frame = tk.LabelFrame(root3, text="Open File")
           file_frame.place(height=100, width=400, rely=0.43, relx=0.05)

           button1 = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
           button1.place(rely=0.65, relx=0.50)

           button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
           button2.place(rely=0.65, relx=0.30)

           label_file = ttk.Label(file_frame, text="No File Selected")
           label_file.place(rely=0, relx=0)

           tv1 = ttk.Treeview(frame1)
           tv1.place(relheight=1,relwidth=1)

           treescrolly = tk.Scrollbar(frame1, orient="vertical",command=tv1.yview)
           treescrollx = tk.Scrollbar(frame1, orient="horizontal",command=tv1.xview)
           tv1.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
           treescrollx.pack(side="bottom", fill="x")
           treescrolly.pack(side="right", fill="y")

           button1 = tk.Button(root3, text='search', command=root2.destroy, bg='brown', fg='black', width=30,
                               font=('helvetica', 9, 'bold'))
           canvas3.create_window(400, 400, window=button1)

           label1 = tk.Label(root3,text='INPUT THE TARGET DATE:')
           label1.config(font=('helvetica', 10))
           canvas3.create_window(100, 380, window=label1)

           self.entry9 = tk.Entry(root3)
           canvas3.create_window(150, 400, window=self.entry9, width=200)

           def File_dialog():
               #This Function will open the file explorer and assign the chosen file path to label_file
               filename = filedialog.askopenfilename(initialdir="/",
                                                     title="Select A File",
                                                     filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))
               label_file["text"] = filename
               return None

           def Load_excel_data():
               #If the file selected is valid this will load the file into the Treeview
               file_path = label_file["text"]
               try:
                   excel_filename = r"{}".format(file_path)
                   if excel_filename[-4:] == ".csv":
                       df = pd.read_csv(excel_filename, engine='openpyxl')
                   else:
                       df = pd.read_excel(excel_filename, engine='openpyxl')

               except ValueError:
                   tk.messagebox.showerror("Information", "The file you have chosen is invalid")
                   return None
               except FileNotFoundError:
                   tk.messagebox.showerror("Information", f"No such file as {file_path}")
                   return None

               clear_data()
               tv1["column"] = list(df.columns)
               tv1["show"] = "headings"
               for column in tv1["columns"]:
                   tv1.heading(column, text=column)  # let the column heading = column name

               df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
               for row in df_rows:
                   tv1.insert("", "end",
                              values=row)  # inserts each list into the treeview
               return None

           def clear_data():
               tv1.delete(*tv1.get_children())
               return None

    def inputData(self):  # trasfering data to the excel
        path = "Info.xlsx"
        df1 = pd.read_excel(path, engine='openpyxl')
        SeriesA = df1['NAME']
        SeriesB = df1['AGE']
        SeriesC = df1['SEX']
        SeriesD = df1['ADDRESS']
        SeriesE = df1['CONTACT']
        SeriesF = df1['DATE']
        SeriesG = df1['TIME']
        SeriesH = df1['Question1']
        SeriesI = df1['Question2']
        SeriesJ = df1['Question3']

        A = pd.Series(self.entry1.get())
        B = pd.Series(self.entry2.get())
        C = pd.Series(self.entry3.get())
        D = pd.Series(self.entry4.get())
        E = pd.Series(self.entry5.get())
        F = pd.Series(strftime('%m-%d-%y'))
        G = pd.Series(strftime('%I:%M:%S%p'))
        H = pd.Series(self.entry6.get())
        I = pd.Series(self.entry7.get())
        J = pd.Series(self.entry8.get())

        SeriesA = SeriesA.append(A)
        SeriesB = SeriesB.append(B)
        SeriesC = SeriesC.append(C)
        SeriesD = SeriesD.append(D)
        SeriesE = SeriesE.append(E)
        SeriesF = SeriesF.append(F)
        SeriesG = SeriesG.append(G)
        SeriesH = SeriesH.append(H)
        SeriesI = SeriesI.append(I)
        SeriesJ = SeriesJ.append(J)
        df2 = pd.DataFrame({"NAME": SeriesA, "AGE": SeriesB, "SEX": SeriesC,
                            "ADDRESS": SeriesD, "CONTACT": SeriesE,
                            "DATE": SeriesF, "TIME": SeriesG,"Question1":SeriesH,"Question2":SeriesI,"Question3":SeriesJ})


        df2.to_excel(path,index=False)

if __name__ == '__main__':
   date = strftime('%m-%d-%y')
   time = strftime('%I:%M%p')
   root = App()
   root.title("SCREENING APP")
   root.resizable(False,False)
   root.home()
   root.mainloop()