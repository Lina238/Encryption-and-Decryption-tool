'''install pybase64 using
pip install pybase64
install 
'''
from tkinter import *
from tkinter import messagebox
import base64
import os
def reset():
          code.set("")
          txt.delete(1.0,END)
def Encrypt():
  password=code.get()
  if password=="linaben":#put your password here 
   screen1=Toplevel(screen)
   screen1.title("Encryption Operation")
   screen1.geometry("400x200")
   screen1.configure(bg="red")
   msg=txt.get(1.0,END)
   enc_msg=msg.encode("ascii")
   base64_byte=base64.b64encode(enc_msg)
   Encrypt=base64_byte.decode("ascii")
   Label(screen1,text="ENCRYPTION",font="calbri",bg="white").place(x=15,y=0)
   txt2=Text(screen1,font="ROBOT 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
   txt2.place(x=15,y=40,width=380,height=150)
   txt2.insert(END,Encrypt)
  elif password=="" or password!="linaben":
    messagebox.showerror("Encryption Operation","Enter your password correctly!")
def Decrypt():
  password=code.get()
  if password=="linaben":#put your password here 
   screen2=Toplevel(screen)
   screen2.title("Decryption Operation")
   screen2.geometry("400x200")
   screen2.configure(bg="green")
   msg=txt.get(1.0,END)
   dec_msg=msg.encode("ascii")
   base64_byte=base64.b64decode(dec_msg)
   decrypt=base64_byte.decode("ascii")
   Label(screen2,text="DECRYPTION",font="calbri",bg="white").place(x=15,y=0)
   txt2=Text(screen2,font="ROBOT 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
   txt2.place(x=15,y=40,width=380,height=150)
   txt2.insert(END,decrypt)
  elif password=="" or password!="linaben":
    messagebox.showerror("Decryption Operation","Enter your password correctly!")          
def mainprogram():
    global screen 
    global code
    global txt 
#let's create our screen
    screen=Tk()
 #size
    screen.geometry("400x400")
 #Icon
    icon=PhotoImage(file="1.png")# add image path here 
    screen.iconphoto(False,icon)
    #Title
    screen.title("ToolApp")
 #labels
    #1-text
    Label(text='ENTER YOUR TEXT',font=("calbri",15),fg="black").place(x=15,y=15)
    txt=Text(font="Robote 15",bg='white',relief=GROOVE,wrap=WORD,bd=0)
    txt.place(x=15,y=60,width=380,height=120)
    #2-password
    Label(text='ENTER YOUR PASSWORD',font=("calbri",15),fg="black").place(x=15,y=190)
    code=StringVar()
    Entry(textvariable=code,width=25,font=("arial",20),bd=0,show='*').place(x=15,y=240)
 #Buttons:
    #1-Encryption
    Button(text="ENCRYPT :)",height="2",width="23",fg="white",bg="red",bd=0,command=Encrypt).place(x=15,y=300)
    Button(text="DECRYPT :)",height="2",width="23",fg="white",bg="green",bd=0,command=Decrypt).place(x=200,y=300)   
    Button(text="RESET:)",height="2",width="50",fg="white",bg="gray",bd=0,command=reset).place(x=15,y=350)                 
    screen.mainloop()

mainprogram()    
