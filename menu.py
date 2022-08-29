
from cgitb import text
from tkinter import*
from traceback import format_tb
from turtle import title
from PIL import Image,ImageTk #pip install pillow


class RMS:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Managment")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #===icons====

        self.logo_dash=ImageTk.PhotoImage(file="image/logo afam.jpg")

        #===title====
        title=Label(self.root,text="Student Result Managment",compound=LEFT, padx=10,image=self.logo_dash, font=("goudy old style",20,"bold"),
        bg="#033054",fg="white").place(x=0, y=0,relwidth=1,height=50) 

        M_frame=LabelFrame(self.root,text="Menu", font=("times new roman",15),bg="white")
        M_frame.place(x=10,y=90,width=1340,height=80)

        bnt_course=Button(M_frame,text="Course",font=("goudy old style",15,"bold"),
        bg="#0b5377",fg="white").place(x=20, y=5, width=200,height=40)
        bnt_sab=Button(M_frame,text="sab",font=("goudy old style",15,"bold"),
        bg="#0b5377",fg="white").place(x=240, y=5, width=200,height=40)
        bnt_pab=Button(M_frame,text="pab",font=("goudy old style",15,"bold"),
        bg="#0b5377",fg="white").place(x=460, y=5, width=200,height=40)
        bnt_loyer=Button(M_frame,text="loyer",font=("goudy old style",15,"bold"),
        bg="#0b5377",fg="white").place(x=680, y=5, width=200,height=40)
        bnt_depense=Button(M_frame,text="depense",font=("goudy old style",15,"bold"),
        bg="#0b5377",fg="white").place(x=900, y=5, width=200,height=40)
        bnt_recette=Button(M_frame,text="recette",font=("goudy old style",15,"bold"),
        bg="#0b5377",fg="white").place(x=1120, y=5, width=200,height=40)


        Mo_frame=LabelFrame(self.root,text="Menu", font=("times new roman",15),bg="white")
        Mo_frame.place(x=10,y=190,width=1340,height=80)

        bnt_course=Button(Mo_frame,text="clickMe",font=("goudy old style",15,"bold"),
        bg="#0b5377",fg="white").place(x=20, y=5, width=200,height=40)
         

        

   
        #===content_window===
         


        #===Footer====
        footer=Label(self.root,text="SRMS-Student Result Managment/nContact Us for any  technical issue:8745xxxxxx ", font=("goudy old style",17,"bold"), bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
     
        


if __name__== "__main__":
    root = Tk()
    obj=RMS(root) 
    root.mainloop()




# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()
        