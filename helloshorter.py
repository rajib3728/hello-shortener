import os
import tkinter as tk
from tkinter import messagebox
import webbrowser
import pyperclip
def hello():
    '''f=open("hello.txt",'a')
    x=e1.get()
    f.write("\n"+str(x))
    f.close()
    f1=open("hello.txt",'r')
    f1.read()
    f1.close()
    op.config(text="got")'''
    if e1.get()=="":
        messagebox.showinfo("info","please provide url first")
    else:
        with open("hello.txt",'r') as file:
            last_line = file.readlines()[-1]
            x=int(last_line)
            x=x+1
        y="hello.shorter/"+str(x)
        f=open("hello.txt",'a')
        f.write("\n"+e1.get())
        f.write("\n"+y)
        f.write("\n"+str(x))
        f.close()
        op.config(text=y)
def cpy():
        if e1.get()=="":
            messagebox.showinfo("info","please provide url first")
        else:
            with open("hello.txt",'r') as file:
                last_line = file.readlines()[-2]
            pyperclip.copy(last_line)
            messagebox.showinfo("info","succesfully copied!")  
def srch():
    if e2.get()=="":
        messagebox.showinfo("info","please provide short url first")
    else:
        a=e2.get()+"\n"
        f=open("hello.txt",'r')
        l=f.readlines()
        for i in range(len(l)):
            if l[i]==a:
                messagebox.showinfo("info","opening: "+str(l[i-1]))
                webbrowser.open(l[i-1])
                break
def hlp():
    messagebox.showinfo("Info",'''
    This is a url shortener.
    Note:
    *This short url only work in this app.
    *If cursor is not touching the last letter
    in search box,it will not work.
    How to use?
    Step 1: provide url and generate short url
    Step 2:Copy the short url for future purpose
    Step 3: Search given shorl url in the search box''')
root=tk.Tk()
root.geometry("400x300")
root.minsize(400,300)
root.maxsize(400,300)
photo = tk.PhotoImage(file = "logo.png")
root.iconphoto(False,photo)
root.title("Hello shorter")
l1=tk.Label(root,text="Welcome to this application",font=50)
l1.grid(row=0,column=1)
l2=tk.Label(root,text="Give url")
e1=tk.Entry(root)
btn1=tk.Button(text="click",command=hello)
l2.grid(row=1,column=0,pady=5)
e1.grid(row=1,column=1,pady=5)
btn1.grid(row=1,column=2,pady=5)
l3=tk.Label(root,text="Output")
l3.grid(row=2,column=0,pady=5)
op=tk.Label(root,text="")
op.grid(row=2,column=1,pady=5)
cp=tk.Button(root,text="copy",command=cpy)
cp.grid(row=2,column=2,pady=5)
l4=tk.Label(root,text="Search url")
e2=tk.Entry(root)
btn2=tk.Button(root,text="search",command=srch)
l4.grid(row=3,column=0,pady=5)
e2.grid(row=3,column=1,pady=5)
btn2.grid(row=3,column=2,pady=5)
btn3=tk.Button(root,text="help",command=hlp)
btn3.grid(row=4,column=1,pady=5)
root.mainloop()
