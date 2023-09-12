from tkinter import *
from tkinter import ttk

# colors

white = "#feffff"  # white/branca
co2 = "#38576b"  
co3 ="#ECEFF1"
co4='#FFAB40' # Orange/laranja

background = "#3b3b3b" # black/preta


window = Tk()
window.title("Calculadora")
window.geometry("235x318")
window.config(background=background)

# Frames

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame = Frame(window, width=300, height=56,bg=co2, pady=0, padx=0, relief="flat")
frame.grid(row=1, column=0, sticky=NW)

body = Frame(window, width=300, height=340,bg=background, pady=0, padx=0, relief="flat")
body.grid(row=2, column=0, sticky=NW)

# Label

screen = Label(window,text='123456789',width=16,height=2, padx=7, relief="flat", anchor="e",bd=0, justify=RIGHT, font=('Ivy 18 '), bg='#37474F', fg=white)
screen.place(x=0, y=0)

# Buttons 

b_clean = Button(body, text="C", width=11, height=2, bg=co3, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_clean.place(x=0, y=0)

b_percent = Button(body, text="%", width=5, height=2, bg=co3, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_percent.place(x=118, y=0)

b_clean = Button(body, text="/", width=5, height=2, bg=co3, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=GROOVE)
b_clean.place(x=177, y=0)



b_seven = Button(body, text="7", width=5, height=2, bg=co3, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_seven.place(x=0, y=52)

b_eigth = Button(body, text="8", width=5, height=2, bg=co3, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_eigth.place(x=59, y=52)

b_nine = Button(body, text="9", width=5, height=2, bg=co3, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_nine.place(x=118, y=52)

b_multiplication = Button(body, text="X", width=5, height=2, bg=co3, fg=background,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_multiplication.place(x=177, y=52)



b_six = Button(body, text="6", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_six.place(x=0, y=104)

b_five = Button(body, text="5", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_five.place(x=59, y=104)

b_four = Button(body, text="4", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_four.place(x=118, y=104)

b_minus = Button(body, text="-", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_minus.place(x=177, y=104)


b_three = Button(body, text="3", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_three.place(x=0, y=156)

b_two = Button(body, text="2", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_two.place(x=59, y=156)

b_one = Button(body, text="1", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_one.place(x=118, y=156)

b_plus = Button(body, text="+", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_plus.place(x=177, y=156)


b_zero = Button(body, text="0", width=11, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_zero.place(x=0, y=208)

b_dot = Button(body, text=".", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_dot.place(x=118, y=208)

b_equals = Button(body, text="=", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=FLAT, overrelief=RIDGE)
b_equals.place(x=177, y=208)


window.mainloop()


