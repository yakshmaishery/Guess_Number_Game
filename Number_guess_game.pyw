from tkinter import *
import random
import tkinter.messagebox as msg
# global variables
a=random.randint(0,50)
b=random.randint(51,100)
nums=random.randint(a,b)
# functions
i=10
def main_func(*args):
    try:
        x=select.get()
        global i,a,b,nums
        i=i-1
        if i==0:
            ask=msg.askquestion("Exit","You Have Lost Do Want to Exit")
            if ask=="yes":
                root.destroy()
            else:
                i=10
                a=random.randint(0,50)
                b=random.randint(51,100)
                nums=random.randint(a,b)
                range_label.config(text=f"The Range is between from {a} to {b}")
                # print(nums)
                select.set(0)
            pass
        if x==nums:
            result.config(text=f"Congradulation you have guessed the right Number",font=("arial",20,"underline","bold"),fg="green",bg="yellow")
            ask=msg.askquestion("Won","You Have Won Do Want to Exit")
            if ask=="yes":
                root.destroy()
            else:
                i=10
                a=random.randint(0,50)
                b=random.randint(51,100)
                nums=random.randint(a,b)
                range_label.config(text=f"The Range is between from {a} to {b}")
                # print(nums)
                select.set(0)
                result.config(text="")
            pass
        elif a>x or x>b:
            result.config(text=f"Out of range from {a} to {b}",fg="green",bg="yellow")
            pass
        elif x<nums:
            result.config(text=f"The number is smaller\n than the actual number",fg="green",bg="yellow")
            pass
        elif x>nums:
            result.config(text=f"The number is Larger\n than the actual number",fg="green",bg="yellow")
            pass
        else:
            result.config(text="",fg="green",bg="yellow")
            pass
        times.config(text=f"No.of Rounds:-{i}")
    except:
        pass
    pass
def upper(*args):
    x=select.get()
    x=x+1
    select.set(x)
    pass
def down(*args):
    x=select.get()
    x=x-1
    if x<=0:
        select.set(0)
        pass
    else:
        select.set(x)
    pass
# main Program
root=Tk()
root.title("Number_Guess")
root.config(bg="yellow")
x_axis=int(root.winfo_screenwidth()/2-root.winfo_reqwidth()*1.2)
y_axis=int(root.winfo_screenheight()/2-root.winfo_reqheight()*0.8)
root.geometry(f"+{x_axis}+{y_axis}")
root.resizable(0,0)
Label(root,text="Guess The Correct Number",font=("arial",25,"bold"),fg="red",bg="yellow").pack(padx=5,pady=5)
# range
range_label=Label(root,text=f"The Range is between from {a} to {b}",font=("arial",15,"bold"),bg="yellow",fg="red")
range_label.pack(padx=5,pady=5)
# times
times=Label(root,text=f"No.of Rounds:-{i}",font=("arial",13,"bold"),bg="yellow",fg="red")
times.pack(padx=5,pady=5)
# entry
select=IntVar()
Value=Entry(root,font=("arial",20,"bold"),borderwidth=2,relief=SOLID,textvariable=select)
Value.pack(padx=5,pady=5)
# submit button
b1=Button(root,text="Submit",font=("arial",20,"bold"),bg="red",fg="white",borderwidth=1,relief=SOLID,cursor="hand2",command=main_func)
b1.pack(padx=5,pady=5)
# result
result=Label(root,text="",font=("arial",20,"bold"),bg="yellow")
result.pack(padx=5,pady=5)

root.bind("<Up>",upper)
root.bind("<Down>",down)
root.bind("<Return>",main_func)
root.mainloop()