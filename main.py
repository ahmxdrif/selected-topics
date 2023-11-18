# print('Lab 3 - Question 1')
# from random import random
# print(random())

# print('Lab 3 - Question 2')
# import random
# list1 = [1,2,3,4,5,6]
# print(random.choice(list1))

# print('Lab 3 - Question 3')
# import random
# random.seed(5)
# print(random.random())
# print(random.random())

# print('Lab 3 - Question 4')
# import random
# r1 = random.randint(5,15)
# print("Random number between 5  and 15 is %s" %(r1))
# r2 = random.randint(-10,-2)
# print("Random number betwwen -10 and -2 is %d" % (r2))

# print('Lab 3 - Question 5')
# from tkinter import *
# from tkinter import messagebox
# root = Tk()
# root.geometry("300x200")
# w = Label(root, text = 'GeeksForGeeks', font = "50")
# w.pack()
# messagebox.showinfo("showinfo", "Information")
# messagebox.showwarning("showwarning", "Warning")
# messagebox.showerror("showerror", "Error")
# messagebox.askquestion("askquestion", "Are you sure?")
# messagebox.askokcancel("askokcancel", "Want to continue?")
# messagebox.askyesno("askyesno", "Find your value?")
# messagebox.askretrycancel("askretrycancel", "Try again?")
# root.mainloop()

# print('Lab 3 - Question 6')
# from tkinter import *
# from tkinter import messagebox

# top = Tk()
# mb = Menubutton(top, text="Course", relief=RAISED)
# mb.grid()
# mb.menu = Menu(mb, tearoff = 0)
# mb["menu"] = mb.menu

# pythonVar = IntVar()
# javaVar = IntVar()

# mb.menu.add_checkbutton(label="Python", variable=pythonVar)
# mb.menu.add_checkbutton(label="Java", variable=javaVar)
# mb.pack()
# top.mainloop()

# print('Lab 3 - Question 7')
# from tkinter import *
# def sel():
#     selection = "You selected the option" + str(var.get())
#     label.config(text=selection)
# root = Tk()
# var = IntVar()
# R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
# R1.pack(anchor=W)
# R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
# R2.pack(anchor=W)
# R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
# R3.pack(anchor=W)
# label = Label(root)
# label.pack()
# root.mainloop()

# print('Lab 3 - Question 8')
# import tkinter as tk
# mast = tk.Tk()
# whatever_you_do = "Welcome to Python Course.\n(Univ. Kuala Lumpur)"
# msg = tk.Message(mast, text=whatever_you_do)
# msg.config(bg="lightgreen", font=('times', 24, 'italic'))
# msg.pack()
# tk.mainloop()

# print('Lab 3 - Question 9')
# from tkinter import *
# from tkinter import ttk
# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass

# root = Tk()
# root.title("Feed to Meters")
# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E,S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W,E))
# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W,E))
# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children():
#     child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)
# root.mainloop()

# print('Lab 3 - Question 10')
# from tkinter import *
# expression = ""
# def press(num):
#     global expression
#     expression = expression + str(num)
#     equation.set(expression)
    
# def equalpress():
#     try:
#         global expression
#         total = str(eval(expression))
#         equation.set(total)
#         expression = ""
#     except:
#         equation.set("error")
#         expression = ""
        
# def clear():
#     global expression
#     expression = ""
#     equation.set("")

# if __name__ == "_main__":
#     gui = Tk()
#     gui.configure(background="lightgreen")
#     gui.title("Simple Calculator")
#     gui.geometry("270x150")
#     equation = StringVar()
#     expression_field = Entry(gui, textvariable=equation)
#     expression_field.grid(columnspan=4, ipadx=70)
#     button1 = Button(gui, text='1', fg='black', bg='lightblue', command=lambda:press(1), height=1, width=7)
#     button1.grid(row=2, column=0)
    
#     button2 = Button(gui, text='2', fg='black', bg='lightblue', command=lambda:press(2), height=1, width=7)
#     button2.grid(row=2, column=1)
    
#     button3 = Button(gui, text='3', fg='black', bg='lightblue', command=lambda:press(3), height=1, width=7)
#     button3.grid(row=2, column=2)
    
#     button4 = Button(gui, text='4', fg='black', bg='lightblue', command=lambda:press(4), height=1, width=7)
#     button4.grid(row=3, column=0)
    
#     button5 = Button(gui, text='5', fg='black', bg='lightblue', command=lambda:press(5), height=1, width=7)
#     button5.grid(row=3, column=1)
    
#     button6 = Button(gui, text='6', fg='black', bg='lightblue', command=lambda:press(6), height=1, width=7)
#     button6.grid(row=3, column=2)
    
#     button7 = Button(gui, text='7', fg='black', bg='lightblue', command=lambda:press(7), height=1, width=7)
#     button7.grid(row=4, column=0)  
    
#     button8 = Button(gui, text='8', fg='black', bg='lightblue', command=lambda:press(8), height=1, width=7)
#     button8.grid(row=4, column=1) 

#     button9 = Button(gui, text='9', fg='black', bg='lightblue', command=lambda:press(9), height=1, width=7)
#     button6.grid(row=4, column=2)   
    
#     button0 = Button(gui, text='0', fg='black', bg='lightblue', command=lambda:press(0), height=1, width=7)
#     button6.grid(row=5, column=0)       
    
#     plus = Button(gui, text='+', fg='black', bg='lightblue', command=lambda:press("+"), height=1, width=7)
#     plus.grid(row=2, column=3)
    
#     minus = Button(gui, text='-', fg='black', bg='lightblue', command=lambda:press('-'), height=1, width=7)
#     minus.grid(row=3, column=3)
    
#     multiply = Button(gui, text='x', fg='black', bg='lightblue', command=lambda:press('*'), height=1, width=7)
#     multiply.grid(row=4, column=3)
    
#     divide = Button(gui, text='/', fg='black', bg='lightblue', command=lambda:press('/'), height=1, width=7)
#     divide.grid(row=5, column=3) 
    
#     equal = Button(gui, text='=', fg='black', bg='lightblue', command=equalpress, height=1, width=7)
#     equal.grid(row=5, column=2) 
    
#     clear = Button(gui, text='Clear', fg='black', bg='lightblue', command=clear, height=1, width=7)
#     clear.grid(row=5, column=1)
    
#     decimal = Button(gui, text='..', fg='black', bg='lightblue', command=lambda:press('.'), height=1, width=7)
#     decimal.grid(row=6, column=0)  
    
#     gui.mainloop()
from tkinter import *

def calculate_charge():
    package_type = package_type_var.get()
    service_type = service_type_var.get()
    weight = float(weight_entry.get())

    if package_type == 1:  # Letter
        if service_type == 1 and weight <= 2:
            charge = 12.00
        elif service_type == 2 and weight <= 4:
            charge = 10.50
        else:
            charge = "Not Available"
    else:  # Box
        if service_type == 1:
            charge = 15.00 + max(0, weight - 1) * 2.00
        elif service_type == 2:
            charge = 11.00 + max(0, weight - 1) * 1.00
        elif service_type == 3:
            charge = 7.00 + max(0, weight - 1) * 0.50

    result_label.config(text=f"Total Charge: RM{charge}")

# GUI Setup
root = Tk()
root.geometry("300x300")
root.title("Expressed Mutiara Delivery Application")

Label(root, text='Expressed Mutiara Delivery Application').pack()

# Package Type Selection
package_type_var = IntVar()
Label(root, text='Select Package Type:').pack()
Radiobutton(root, text="Letter", variable=package_type_var, value=1).pack()
Radiobutton(root, text="Box", variable=package_type_var, value=2).pack()

# Service Type Selection
service_type_var = IntVar()
Label(root, text='Select Service Type:').pack()
Radiobutton(root, text="Next Day Priority", variable=service_type_var, value=1).pack()
Radiobutton(root, text="Next Day Standard", variable=service_type_var, value=2).pack()
Radiobutton(root, text="2-Day", variable=service_type_var, value=3).pack()

# Weight Entry
Label(root, text='Enter Weight (kg):').pack()
weight_entry = Entry(root)
weight_entry.pack()

# Calculate Button
Button(root, text="Calculate Charge", command=calculate_charge).pack()

# Result Label
result_label = Label(root, text="Total Charge: ")
result_label.pack()

root.mainloop()

