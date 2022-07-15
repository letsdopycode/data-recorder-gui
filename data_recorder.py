from tkinter import *
import tkinter as tk
from tkinter import messagebox
win=tk.Tk()
win.geometry("650x450+100+100")
win.configure(bg="#006400")
win.title("file handling")

def read_file():
        win1=tk.Tk()
        win1.geometry("550x350+100+100")
        win1.configure(bg="#006400")
        win1.title("read file")
        file=open("a1.txt",mode="r")
        # print(file.read())
        read=file.read()
        # messagebox.showinfo("read data",read)
        text_box=Text(win1,height=5,width=100,bg="#006400",fg="#00FF7F")
        text_box.place(x=0,y=100)
        text_box.insert(INSERT,read)
        Label(win1,text="showing data in a1.txt",bg="#006400",fg="#00FF7F",font="bold 10").place(x=140,y=60)
        Button(win1,text="exit",width=17,height=2,bg="#006400",fg="#00FF7F",command=win1.destroy).place(x=150,y=200)
        win1.mainloop()

def write_file():
        def update_changes():
                file=open("a1.txt",mode="w")
                i=StringVar()
                i=e1.get()
                print(file.write(i))
                file.close()
                # l=Label(win,text="updated file successfully!!",bg="white",fg="black")
                # l.plssagebox.sace(x=230,y=410)
                messagebox.showinfo("updated file", "successfully store data!!")
                e1.delete(0,END)

        global e1
        l=Label(win,text="write here",bg="#006400",fg="#00FF7F",font="bold 13")
        l.place(x=280,y=250)
        Button(win,text="update file",width=17,height=2,bg="#006400",fg="#00FF7F",command=update_changes,font="bold 10").place(x=280,y=350)

        e1=Entry(win,width=40)
        e1.place(x=200,y=300)


def append_file():
        def update_changes():
                j=StringVar()
                j=e2.get()
                file=open("a1.txt",mode="a")
                print(file.write(j))
                file.close()
                # l1=Label(win,text="updated file successfully!!",bg="white",fg="black")
                # l1.place(x=230,y=410)
                messagebox.showinfo("updated file", "data appended successfully!!!!!")
                e2.delete(0,END)

        global e2
        Button(win,text="update file",width=17,height=2,bg="#006400",fg="#00FF7F",command=update_changes,font="bold 10").place(x=280,y=350)
        e2=Entry(win,width=40)
        e2.place(x=200,y=300)
        
        
Label(win,text="perform file operations",width=30,height=2,bg="#006400",fg="#00FF7F",font="bold 14").pack()
#create buttons  to perform read,write and append operation 
Button(win,text="read file",width=15,height=2,bg="#006400",fg="#00FF7F",command=read_file,font="bold 10").place(x=50,y=100)
Button(win,text="write data",width=15,height=2,bg="#006400",fg="#00FF7F",command=write_file,font="bold 10").place(x=200,y=100)
Button(win,text="append data",width=15,height=2,bg="#006400",fg="#00FF7F",command=append_file,font="bold 10").place(x=350,y=100)
Button(win,text="exit",width=12,height=2,bg="#006400",fg="#00FF7F",command=win.destroy,font="bold 10").place(x=500,y=100)


# execute window
win.mainloop()
