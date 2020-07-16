from tkinter import *
from tkinter import messagebox,Toplevel
import pyqrcode
import png
import os

root = Tk()
root.geometry('570x400')
root.title('QR CODE Genarator')
#root.wm_iconbitmap('QR.ico')
root.configure(bg='#fff')
#functions
def Generate_Qr():
    #qr_name = qr_name_entry.get()
    qr_mssge= qr_mssge_entry.get()
    mssge_qr="message: "+qr_mssge
    url=pyqrcode.create(mssge_qr)

    pa = r"C:\Users\iamkb\Desktop\QR"
    cc = '{}.png'.format(pa)
    
    li=os.listdir(pa)
    if('{}.png'.format(qr_mssge) in li):
        messagebox.showinfo("notofication","please choose another name or id")
    else:
        url.png(cc,scale=8)
        mm =".png"
        qr_notification_mssge_label.config(text=mm)
        res=messagebox.askyesno("Notification","QR code is generated")
        if(res==True):
            top=Toplevel()
            top.geometry("400x400")
            top.configure(bg="white")
            img=PhotoImage(file=cc)
            Label1 = Label(top,image=img,bg="white")
            Label1.place(x=10,y=10)
            top.mainloop()

#titles

qr_mssge_label = Label(master=root,text="enter your mssge: ",bg="powder blue",fg="red",width=60,height=2,font=("times",12,"italic bold"))
qr_mssge_label.place(x=10,y=10)
#text area

qr_mssge_entry=Entry(master=root,width=25,bd=5,bg="pink",font=("times",27,"italic bold"))
qr_mssge_entry.place(x=50,y=128)

#button
generate_QR_button = Button(master=root,text="GENERATE",width=15,font=("times",10,"italic bold"),bd=10,activebackground="blue",bg="powder blue",compound=RIGHT,command=Generate_Qr)
generate_QR_button.place(x=200,y=250)




#notofication
qr_notification_label = Label(master=root,text="enter your notification: ",bg="powder blue",fg="red",width=25,height=2,font=("times",15,"bold underline"))
qr_notification_label.place(x=10,y=350)
#status
qr_notification_mssge_label = Label(master=root,text=" ",bg="powder blue",fg="red",width=20,height=2,font=("times",15,"bold "))
qr_notification_mssge_label.place(x=300,y=350)

#hover
def generate_QR_buttonEnter(e):
    generate_QR_button["bg"] = "pink"
def generate_QR_buttonLeave(e):
    generate_QR_button["bg"] = "powder blue"

generate_QR_button.bind("<Enter>",generate_QR_buttonEnter)
generate_QR_button.bind("<Leave>",generate_QR_buttonLeave)


root.mainloop()