import tkinter as tk
def exit():
    window.destroy()

def add():
    a=float(Entry1.get())
    b=float(Entry2.get())
    result = a+b
    Entry3.configure(state='normal')
    Entry3.delete(0,tk.END)
    Entry3.insert(0,result)
    Entry3.configure(state='disabled')

def sub():
    a=float(Entry1.get())
    b=float(Entry2.get())
    result = a-b
    Entry3.configure(state='normal')
    Entry3.delete(0,tk.END)
    Entry3.insert(0,result)
    Entry3.configure(state='disabled')

def multiply():
    a=float(Entry1.get())
    b=float(Entry2.get())
    result = a*b
    Entry3.configure(state='normal')
    Entry3.delete(0,tk.END)
    Entry3.insert(0,result)
    Entry3.configure(state='disabled')

def divide():
    a=float(Entry1.get())
    b=float(Entry2.get())
    result = a/b
    Entry3.configure(state='normal')
    Entry3.delete(0,tk.END)
    Entry3.insert(0,result)
    Entry3.configure(state='disabled')

def remainder():
    a=float(Entry1.get())
    b=float(Entry2.get())
    result = a%b
    Entry3.configure(state='normal')
    Entry3.delete(0,tk.END)
    Entry3.insert(0,result)
    Entry3.configure(state='disabled')

def clear():
    Entry1.delete(0,tk.END)
    Entry2.delete(0,tk.END)
    Entry3.configure(state='normal')
    Entry3.delete(0,tk.END)
    Entry3.configure(state='disabled')

window=tk.Tk()
window.title("simple calculator")

Label1 = tk.Label(window, text="enter first number:")
Label1.grid(row=0, column=0)
Entry1 = tk.Entry(window)
Entry1.grid(row=0, column=1)
Label2 = tk.Label(window, text="enter second number:")
Label2.grid(row=1, column=0)
Entry2 = tk.Entry(window)
Entry2.grid(row=1, column=1)
Label3 = tk.Label(window, text="Result:")
Label3.grid(row=2, column=0)
Entry3 = tk.Entry(window)
Entry3.grid(row=2, column=1)
Button1 = tk.Button(window, text="add", command=add)
Button1.grid(row=3, column=0)
Button2= tk.Button(window, text="sub", command=sub)
Button2.grid(row=3, column=1)
Button3 = tk.Button(window, text="multiply", command=multiply)
Button3.grid(row=4, column=0)
Button4 = tk.Button(window, text="divide", command=divide)
Button4.grid(row=4, column=1)
Button4 = tk.Button(window, text="remainder", command=remainder)
Button4.grid(row=5, column=0)
Button5 = tk.Button(window, text="clear", command=clear)
Button5.grid(row=5, column=1)
Button6 = tk.Button(window, text="exit", command=exit)
Button6.grid(row=6, column=0)

window.mainloop()

