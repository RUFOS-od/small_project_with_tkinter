
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #PIp install pillow


class Login:
    def __init__(self,root): 
        self.root=root
        self.root.title("Formulaire")
        self.root.geometry("1350x700+0+0") 
        self.root.config(bg="white")

        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="image/compa2.jpg")  
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #===Left image===
        self.left=ImageTk.PhotoImage(file="image/compta.jpg")  
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        #===register form===
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700, height=500)

        #--------------row1

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),
        bg="white",fg="green").place(x=50,y=30)

        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),
        bg="white",fg="gray").place(x=50,y=100)
        txt_fname=Entry(frame1,font=("times new roman ",15),bg="lightgray").place(x=50,y=130,width=250)  

        L_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),
        bg="white",fg="gray").place(x=370,y=100)
        txt_Lname=Entry(frame1,font=("times new roman ",15),bg="lightgray").place(x=370,y=130,width=250) 

        #--------------row2

        contact=Label(frame1,text="Contact",font=("times new roman",15,"bold"),
        bg="white",fg="gray").place(x=50,y=170)
        txt_contact=Entry(frame1,font=("times new roman ",15),bg="lightgray").place(x=50,y=200,width=250) 

        montant_lettre=Label(frame1,text="Montant en Lettre",font=("times new roman",15,"bold"),
        bg="white",fg="gray").place(x=370,y=170)
        txt_montant_lettre=Entry(frame1,font=("times new roman ",15),bg="lightgray").place(x=370,y=200,width=250) 

         
        #--------------row3
   
        centre_de_control=Label(frame1,text="Centre de control",font=("times new roman",15,"bold"),
        bg="white",fg="gray").place(x=50,y=240)

        cmb_centre_de_control=ttk.Combobox(frame1,font=("times new roman ",13))
        cmb_centre_de_control['values']=("select", "S.AB","P.AB","Loyer","Depense","Recette")
        cmb_centre_de_control.place(x=50,y=270,width=250) 
        cmb_centre_de_control.current(0)

        montant_ciffre=Label(frame1,text="Montant en Chiffre",font=("times new roman",15,"bold"),
        bg="white",fg="gray").place(x=370,y=240)
        txt_montant_ciffre=Entry(frame1,font=("times new roman ",15),bg="lightgray").place(x=370,y=270,width=250) 


        #terms--------------

        chk=Checkbutton(frame1,text="I gree the terms & conditions",onvalue=1,offvalue=0,bg="white",).place(x=50,y=380,width=250)

        bnt_valider=Button(frame1,text="Valider",font=("goudy old style",15,"bold"),
        bg="#0b5377",fg="white", cursor="hand2").place(x=50, y=420, width=240,height=40)

        bnt_button=Button(self.root,text="Sign in",font=("goudy old style",20,"bold"),
        bg="#0b5377",fg="white",bd=0 ,cursor="hand2").place(x=200, y=480, width=150 )








ht=40



     
root=Tk()
obj=Login(root)
root.mainloop()