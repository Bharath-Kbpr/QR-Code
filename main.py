from tkinter import *
from tkinter import messagebox,Toplevel
import pyqrcode
import png
import os

root = Tk()
root.geometry('570x400')
root.title('QR CODE Genarator')
#root.wm_iconbitmap('QR.ico')
root.configure(bg='blue')
#functions
def Generate_Qr():
    qr_name = qr_name_entry.get()
    qr_mssge= qr_mssge_entry.get()
    mssge_qr="message: "+qr_mssge
    url=pyqrcode.create(mssge_qr)
    pa = r"C:\Users\iamkb\Desktop\qr"
    cc = '{}\{}.png'.format(pa,qr_mssge)
    
    li=os.listdir(pa)
    if('{}.png',format(qr_mssge) in li):
        messagebox.showinfo("notofication","please those another name or id")
    else:
        url.png(cc,scale=8)
        mm = "Qr Code saved as:"+qr_name+".png"
        qr_notification_mssge_label.config(text=mm)
        res=messagebox.askyesno("Notification","QR code is generated")
        if(res==true):
            top=Toplevel()
            top.geometry("400x400")
            top.configure(bg="white")
            img=PhotoImage(file=cc)
            Label1 = Label(top,Image=img,bg="white")
            Label1.place(x=10,y=10)
            top.mainloop()

#titles
qr_id_label = Label(master=root,text="enter your ID: ",bg="powder blue",fg="red",width=20,height=2,font=("times",12,"italic bold"))
qr_id_label.place(x=10,y=20)
qr_name_label = Label(master=root,text="enter your name: ",bg="powder blue",fg="red",width=20,height=2,font=("times",12,"italic bold"))
qr_name_label.place(x=10,y=80)
qr_mssge_label = Label(master=root,text="enter your mssge: ",bg="powder blue",fg="red",width=20,height=2,font=("times",12,"italic bold"))
qr_mssge_label.place(x=10,y=140)
#text area
qr_id_entry=Entry(master=root,width=25,bd=5,bg="pink",font=("times",17,"italic bold"))
qr_id_entry.place(x=250,y=20)
qr_name_entry=Entry(master=root,width=25,bd=5,bg="pink",font=("times",17,"italic bold"))
qr_name_entry.place(x=250,y=80)
qr_mssge_entry=Entry(master=root,width=25,bd=5,bg="pink",font=("times",17,"italic bold"))
qr_mssge_entry.place(x=250,y=140)
#logo
generate_QR_image = PhotoImage(file="qr-code.png")
generate_QR_image = generate_QR_image.subsample(2,2)
#button
generate_QR_button = Button(master=root,text="GENERATE",width=100,font=("times",10,"italic bold"),bd=10,activebackground="blue",bg="powder blue",image=generate_QR_image,compound=RIGHT,command=Generate_Qr)
generate_QR_button.place(x=10,y=250)
clear_id_button = Button(master=root,text="CLEAR",width=15,font=("times",10,"italic bold"),bd=10,activebackground="blue",bg="powder blue")
clear_id_button.place(x=210,y=250)

quit_id_button = Button(master=root,text="QUIT",width=15,font=("times",10,"italic bold"),bd=10,activebackground="blue",bg="powder blue")
quit_id_button.place(x=410,y=250)

qr_name_label = Label(master=root,text="enter your name: ",bg="powder blue",fg="red",width=20,height=2,font=("times",12,"italic bold"))
qr_name_label.place(x=10,y=80)
qr_mssge_label = Label(master=root,text="enter your mssge: ",bg="powder blue",fg="red",width=20,height=2,font=("times",12,"italic bold"))
qr_mssge_label.place(x=10,y=140)
qr_notification_label = Label(master=root,text="enter your notification: ",bg="powder blue",fg="red",width=10,height=2,font=("times",15,"bold underline"))
qr_notification_label.place(x=10,y=350)
qr_notification_mssge_label = Label(master=root,text=" ",bg="powder blue",fg="red",width=30,height=2,font=("times",15,"bold "))
qr_notification_mssge_label.place(x=200,y=350)

#hover
def generate_QR_buttonEnter(e):
    generate_QR_button["bg"] = "purple2"
def generate_QR_buttonLeave(e):
    generate_QR_button["bg"] = "powder blue"

generate_QR_button.bind("<Enter>",generate_QR_buttonEnter)
generate_QR_button.bind("<Leave>",generate_QR_buttonLeave)


root.mainloop()