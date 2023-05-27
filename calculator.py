from tkinter import *
import tkinter.messagebox
cal = Tk()
num1 = StringVar()
num2 = StringVar()
res = StringVar()
cal.title('calculator')
cal.geometry('400x200')
cal.resizable(width=False,height=False)
color = 'gray'
cal.configure(bg=color)
top_first = Frame(cal, width=400,height=50,bg=color)
top_first.pack(side='top')
top_second = Frame(cal, width=400,height=50,bg=color)
top_second.pack(side='top')
top_third = Frame(cal, width=400,height=50,bg=color)
top_third.pack(side='top')
top_forth = Frame(cal, width=400,height=50,bg=color)
top_forth.pack(side='top')
top_five = Frame(cal, width=400,height=50,bg=color)
top_five.pack(side='top')
btn_minus = Button(top_forth,text="-", width=10 , highlightbackground=color , command=lambda : minus())
btn_minus.pack(side=LEFT , padx=5 , pady=5)
btn_plus = Button(top_forth,text="+", width=10 , highlightbackground=color , command=lambda : plus())
btn_plus.pack(side=LEFT , padx=5 , pady=5)
btn_MUL = Button(top_forth,text="*", width=10 , highlightbackground=color , command=lambda : mul())
btn_MUL.pack(side=LEFT , padx=5 , pady=5)
btn_div = Button(top_forth,text="/", width=10 , highlightbackground=color , command=lambda : div())
btn_div.pack(side=LEFT , padx=5 , pady=5)
btn_clear = Button(top_five,text="clear", width=10 , highlightbackground=color ,command=lambda : clear())
btn_clear.pack(side=LEFT , padx=5 , pady=5)
btn_creator = Button(top_five,text="creator", width=10 , highlightbackground=color , command=lambda : creator())
def errorMSG(ms):
    if ms == "error":
        tkinter.messagebox.showerror('Error','somthing went wrong')   
    elif ms == 'division error':
        tkinter.messagebox.showerror('Division error','cant not divide by 0!')
def plus():
    try:
        value = float(num1.get())+float(num2.get())
        res.set(value)
    except:
        errorMSG('error')
def minus():
    try:
        value = float(num1.get())-float(num2.get())
        res.set(value)
    except:
        errorMSG('error')
def mul():
    try:
        value = float(num1.get())*float(num2.get())
        res.set(value)
    except:
        errorMSG('error')
def div():
    if num2.get() == '0':
        errorMSG('division error')
    elif num2.get() != '0':
        try:
            value = float(num1.get()) / float(num2.get())
            res.set(value)
        except:
            errorMSG('error')
def clear():
    num1.set('')
    num2.set('')
    res.set('')

def creator():
    tkinter.messagebox.showinfo("creator",'this calculator has been created by rezadrakhshan')

        

btn_creator.pack(side=LEFT , padx=5 , pady=5)
label_first_num = Label(top_first,text="enter your first number",bg=color)
label_first_num.pack(side=LEFT,padx=5,pady=5)
first_num = Entry(top_first,highlightbackground=color ,textvariable=num1)
first_num.pack(side=LEFT)
label_second_num = Label(top_second,text="enter your second number",bg=color)
label_second_num.pack(side=LEFT,padx=5,pady=5)
second_num = Entry(top_second,highlightbackground=color ,textvariable=num2)
second_num.pack(side=LEFT)
label_result= Label(top_third,text="result",bg=color)
label_result.pack(side=LEFT,padx=5,pady=5)
result = Entry(top_third,highlightbackground=color ,textvariable=res)
result.pack(side=LEFT)
cal.mainloop()