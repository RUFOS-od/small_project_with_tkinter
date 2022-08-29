from cProfile import label
from tkinter import*
from tkinter import messagebox
from unicodedata import name

from cgitb import text
from traceback import format_tb
from turtle import title
from PIL import Image,ImageTk #pip install pillow

def signup(root):
    root.title("Sign up")
    root.geometry("925x500+300+200")
    root.configure(bg="black")
    root.resizable(False,False)    
    
    # insertion d'image de la page signup
    img = PhotoImage(file="login.png")
    Label(root,image=img, bg="white").place(x=50,y=50)

    #création du frame de la page signup
    frame = Frame(root,width=350,height=350, bg="black")
    frame.place(x=480,y=70)

    # creation de Sign de la page signup
    heading = Label(frame, text="Sign Up",fg="black",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
    heading.place(x=100,y=5)
    # creation des champs d'entrées de la page signup

    #creation de fonction évenement de la page signup
    def on_enter(e):
        user.delete(0,'end')
    
    def on_leave(e):
        name = user.get()
        if name =="":
            user.insert(0,"Username")

    #===========username de la page signup
    user = Entry(frame,width=25,fg="white", border=0,bg='black',font=("Microsoft YaHei UI Light",11))
    user.place(x=30,y=80)
    user.insert(0,"Username")
    # creation d'evenement de la page signup
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)


    Frame(frame,width=295,height=2,bg="white").place(x=25,y=107)

        #===========password de la page signup
    def on_enter(e):
        code.delete(0,'end')
    
    def on_leave(e):
        name = code.get()
        if name =="":
            code.insert(0,"Password")

    code = Entry(frame,width=25,fg="white", border=0,bg='black',font=("Microsoft YaHei UI Light",11))
    code.place(x=30,y=130)
    code.insert(0,"Password")
    # creation d'evenement de la page signup
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)
    Frame(frame,width=295,height=2,bg="white").place(x=25,y=157)
    
    
    def on_enter(e):
        code_conf.delete(0,'end')
    
    def on_leave(e):
        name = code_conf.get()
        if name =="":
            code_conf.insert(0,"Password conf")
    
    code_conf = Entry(frame,width=25,fg="white", border=0,bg='black',font=("Microsoft YaHei UI Light",11))
    code_conf.place(x=30,y=180)
    code_conf.insert(0,"Password conf")
    # creation d'evenement de la page signup
    code_conf.bind("<FocusIn>",on_enter)
    code_conf.bind("<FocusOut>",on_leave)
    Frame(frame,width=295,height=2,bg="white").place(x=25,y=207)


    # Creation de button de la page signup

    Button(frame,width=39,pady=6,text="Envoyer", bg="#57a1f8",fg="white",border=0).place(x=35,y=245)
    label = Label(frame,text="Vous avez un compte ?", fg="blue", bg="white",font=("Microsoft YaHei UI Light",9))
    label.place(x=75,y=293)


    sign_up = Button(frame,width=6,text="Sign in", bg="#57a1f8",fg="white",border=0,cursor="hand2")
    sign_up.place(x=250,y=293)
