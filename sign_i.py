from cProfile import label
from tkinter import*
from tkinter import messagebox
from unicodedata import name

from cgitb import text
from traceback import format_tb
from turtle import title
from PIL import Image,ImageTk #pip install pillow

from sign_up import *
from menu import*

def start(root):
    
    def signin():
        username= user.get()
        password = code.get()
        
        if username == "admin" and password =="admin":
            print("Bienvenue")
            
        elif username != "admin" and password !="admin":
            messagebox.showerror("Invalide", "Username et/ou Password invalide")
    
    
    
    root=Tk()
    root.title("Login")
    root.geometry("925x500+300+200")
    root.configure(bg="black")
    root.resizable(False,False)
    
    # insertion d'image
    img = PhotoImage(file="login.png")
    Label(root,image=img, bg="white").place(x=50,y=50)

    #création du frame
    frame = Frame(root,width=350,height=350, bg="black")
    frame.place(x=480,y=70)

    # creation de Sign
    heading = Label(frame, text="Sign in",fg="black",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
    heading.place(x=100,y=5)
    # creation des champs d'entrées

    #creation de fonction
    def on_enter(e):
        user.delete(0,'end')
    
    def on_leave(e):
        name = user.get()
        if name =="":
            user.insert(0,"Username")

    #===========username
    user = Entry(frame,width=25,fg="white", border=0,bg='black',font=("Microsoft YaHei UI Light",11))
    user.place(x=30,y=80)
    user.insert(0,"Username")
    # creation d'evenement
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)


    Frame(frame,width=295,height=2,bg="white").place(x=25,y=107)

    #===========password
    def on_enter(e):
        code.delete(0,'end')
    
    def on_leave(e):
        name = code.get()
        if name =="":
            code.insert(0,"Password")

    code = Entry(frame,width=25,fg="white", border=0,bg='black',font=("Microsoft YaHei UI Light",11))
    code.place(x=30,y=150)
    code.insert(0,"Password")
    # creation d'evenement
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)
    Frame(frame,width=295,height=2,bg="white").place(x=25,y=177)


    # Creation de button

    Button(frame,width=39,pady=7,text="Sign in", bg="#57a1f8",fg="white",border=0,command=lambda: change(root)).place(x=35,y=204)
    label = Label(frame,text="Vous n'avez pas de compte ?", fg="blue", bg="white",font=("Microsoft YaHei UI Light",9))
    label.place(x=75,y=270)


    sign_up = Button(frame,width=6,text="Sign up", bg="#57a1f8",fg="white",border=0,cursor="hand2",command=signup)
    sign_up.place(x=250,y=270)

    


def change(root):
    root.destroy()
    signup()

    
    
def call():
    root=Tk()
    start(root)
    root.mainloop()
    
call()