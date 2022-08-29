from cProfile import label
from tkinter import*
from tkinter import messagebox
from unicodedata import name

from cgitb import text
from traceback import format_tb
from turtle import title
from PIL import Image,ImageTk #pip install pillow



root=Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="black")
root.resizable(False,False)



def signin():
    username= user.get()
    password = code.get()
    
    if username == "admin" and password =="admin":
        corps =Toplevel(root) 
        corps.title("Student Result Managment")
        corps.geometry("1350x700+0+0")
        corps.config(bg="white")
                #===icons====

        logo_dash=ImageTk.PhotoImage(file="image/logo afam.jpg")

                #===title====
        title=Label(corps,text="Student Result Managment",compound=LEFT, padx=10,image=logo_dash, font=("goudy old style",20,"bold"),
        bg="#033054",fg="white").place(x=0, y=0,relwidth=1,height=50) 

        M_frame=LabelFrame(corps,text="Menu", font=("times new roman",15),bg="white")
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


        Mo_frame=LabelFrame(corps,text="Menu", font=("times new roman",15),bg="white")
        Mo_frame.place(x=10,y=190,width=1340,height=80)

        bnt_course=Button(Mo_frame,text="clickMe",font=("goudy old style",15,"bold"),
        bg="#0b5377",fg="white").place(x=20, y=5, width=200,height=40)
         

        

   
                #===content_window===
         


                #===Footer====
        footer=Label(corps,text="SRMS-Student Result Managment/nContact Us for any  technical issue:8745xxxxxx ", font=("goudy old style",17,"bold"), bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
     
        


         
        corps.mainloop()
        
    elif username != "admin" and password !="admin":
        messagebox.showerror("Invalide", "Username et/ou Password invalide")







# fonction de la page Sign up

def signup():
    corps =Toplevel(root) 
    corps.title("Sign up")
    corps.geometry("925x500+300+200")
    corps.configure(bg="black")
    corps.resizable(False,False)
    
    # insertion d'image de la page signup
    img = PhotoImage(file="login.png")
    Label(corps,image=img, bg="white").place(x=50,y=50)

    #création du frame de la page signup
    frame = Frame(corps,width=350,height=350, bg="black")
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


    sign_up = Button(frame,width=6,text="Sign in", bg="#57a1f8",fg="white",border=0,cursor="hand2",command=signin)
    sign_up.place(x=250,y=293)

    corps.mainloop()
    
# Fin de la fonction qui appel la page Sign Up
    


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

Button(frame,width=39,pady=7,text="Sign in", bg="#57a1f8",fg="white",border=0,command=signin).place(x=35,y=204)
label = Label(frame,text="Vous n'avez pas de compte ?", fg="blue", bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=75,y=270)


sign_up = Button(frame,width=6,text="Sign up", bg="#57a1f8",fg="white",border=0,cursor="hand2",command=signup)
sign_up.place(x=250,y=270)

root.mainloop()