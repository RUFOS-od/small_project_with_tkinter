
from tkinter import*
from turtle import title
from tkinter import messagebox

class Connecter:
    def __init__(self,root):
        self.root=root
        self.root.title("Connexion")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")  

        #======Background colors=======
    
        left_lbl=Label(self.root,bg="red",bd=0)  
        left_lbl.place(x=0,y=0,relheight=1,relwidth=600)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)  
        right_lbl.place(x=0,y=0,relheight=1,relwidth=600)

        #======Frames=======
        connect_frame=Frame(self.root,bg="gray")
        connect_frame.place(x=250,y=100,width=800,height=500)



        title=Label(connect_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),
        bg="white",fg="#08A3D2").place(x=250,y=50)

        email=Label(connect_frame,text="Email Adress",font=("times new roman",18,"bold"),
        bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(connect_frame,font=("times new roman",15),bg="white").place(x=250,y=180,width=350,height=35)

        pass_=Label(connect_frame,text="PASSWORD",font=("times new roman",18,"bold"),
        bg="white",fg="gray").place(x=250,y=250)
        self.txt_pass=Entry(connect_frame,font=("times new roman",15),bg="white").place(x=250,y=280,width=350,height=35)


        btn_reg=Button(connect_frame,cursor="hand2",text="Register a new Account?",font=("times new roman",14),fg="white",bg="#B00857")

        btn_forget=Button(connect_frame,cursor="hand2",text="forget paswword?",font=("times new roman",14),fg="white",bg="red")

        btn_connect=Button(connect_frame,text="Enregister",font=("times new roman",20,"bold"),fg="white",bg="#B00857", cursor="hand2").place(x=250,y=360,width=180,height=40)




   



      



root=Tk()
obj=Connecter(root)
root.mainloop()