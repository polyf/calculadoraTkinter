from tkinter import *
from tkinter import ttk

# Colors

white = "#feffff"
grey = "#38576b"  
blue ='#2D82B7' # Operator Color

background = "#3b3b3b" # Black


window = Tk()
window.title("Calculadora")
window.geometry("235x318")
window.config(background=background)

# Variables

values = ""
entry = StringVar()

# Functions

def entry_values(event):
    global values
    values = values + str(event)
    entry.set(values)

def calculate():
    global values
    result = str(eval(values))
    entry.set(result)
    values = ""

def clean_values():
    global values
    values = ""
    entry.set("")

# Frames

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame = Frame(window, width=300, height=56,bg=grey, pady=0, padx=0, relief="flat")
frame.grid(row=1, column=0, sticky=NW)

body = Frame(window, width=300, height=340,bg=background, pady=0, padx=0, relief="flat")
body.grid(row=2, column=0, sticky=NW)

# Label

screen = Label(window,textvariable=entry, width=16,height=2, padx=7, relief="flat", anchor="e",bd=0, 
               justify=RIGHT, font=('Ivy 18 '), bg='#212738', fg=white)
screen.place(x=0, y=0)

# Buttons 

b_clean = Button(body, command = lambda: clean_values(), text="C", width=11, height=2, 
                 bg=white, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_clean.place(x=0, y=0)
b_percent = Button(body, command = lambda: entry_values('%'), text="%", width=5, height=2, 
                   bg=white, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_percent.place(x=118, y=0)
b_clean = Button(body, command = lambda: entry_values('/'), text="/", width=5, height=2, 
                 bg=blue, fg=white,font=('Ivy 13 bold'),relief=FLAT, overrelief=GROOVE)
b_clean.place(x=177, y=0)


b_seven = Button(body, command = lambda: entry_values('7'), text="7", width=5, height=2, 
                 bg=white, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_seven.place(x=0, y=52)
b_eigth = Button(body, command = lambda: entry_values('8'), text="8", width=5, height=2, 
                 bg=white, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_eigth.place(x=59, y=52)
b_nine = Button(body, command = lambda: entry_values('9'), text="9", width=5, height=2, 
                bg=white, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_nine.place(x=118, y=52)
b_multiplication = Button(body, command = lambda: entry_values('*'), text="*", width=5, height=2, 
                bg=blue, fg=white,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_multiplication.place(x=177, y=52)



b_six = Button(body, command = lambda: entry_values('6'), text="6", width=5, height=2, 
               bg=white, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_six.place(x=0, y=104)
b_five = Button(body, command = lambda: entry_values('5'), text="5", width=5, height=2, 
                bg=white, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_five.place(x=59, y=104)
b_four = Button(body, command = lambda: entry_values('4'), text="4", width=5, height=2, 
                bg=white, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_four.place(x=118, y=104)
b_minus = Button(body, command = lambda: entry_values('-'), text="-", width=5, height=2, 
                 bg=blue, fg=white,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_minus.place(x=177, y=104)


b_three = Button(body, command = lambda: entry_values('3'), text="3", width=5, height=2, 
                 bg=white, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_three.place(x=0, y=156)
b_two = Button(body, command = lambda: entry_values('2'), text="2", width=5, height=2, 
               bg=white, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_two.place(x=59, y=156)
b_one = Button(body, command = lambda: entry_values('1'), text="1", width=5, height=2, 
               bg=white, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_one.place(x=118, y=156)
b_plus = Button(body, command = lambda: entry_values('+'), text="+", width=5, height=2, 
                bg=blue, fg=white,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_plus.place(x=177, y=156)


b_zero = Button(body, command = lambda: entry_values('0'), text="0", width=11, height=2, 
                bg=white, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_zero.place(x=0, y=208)
b_dot = Button(body, command = lambda: entry_values('.'), text=".", width=5, height=2, 
               bg=white, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_dot.place(x=118, y=208)
b_equals = Button(body, command = lambda: calculate(), text="=", width=5, height=2, 
                  bg=blue, fg=white,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_equals.place(x=177, y=208)


# Mainloop

window.mainloop()


