from tkinter import *
from tkinter import messagebox

mainwindow = Tk()
mainwindow.title('BMI CALCULATOR')
mainwindow.geometry('500x450')
mainwindow.config(bg='darkcyan')

title_label = Label(mainwindow, text='BMI CALCULATOR', fg='black', bg='white', font=('Arial', 20))
title_label.pack(pady=50,padx=30)

def calbmi():
    kg=int(weighttextfield.get())
    m=int(heighttextfield.get())/100
    bmi=kg/(m*m)
    bmi=round(bmi,1)
    solu(bmi)

def solu(bmi):
    if bmi<18.5:
        messagebox.showinfo('BMI CALCULATOR',f'BMI = {bmi} is UNDERWEIGHT')
    elif bmi>=18.5 and bmi<24.9:
        messagebox.showinfo('BMI CALCULATOR',f'BMI = {bmi} is NORMAL')
    elif bmi>=24.9 and bmi<29.9:
        messagebox.showinfo('BMI CALCULATOR',f'BMI = {bmi} is OVERWEIGHT')
    elif bmi>=29.9:
        messagebox.showinfo('BMI CALCULATOR',f'BMI = {bmi} is OBESITY')
    else:
        messagebox.showerror('BMI CALCULATOR ','SOMETHING WENT WRONG ! ')


def resetfun():
    agetextfield.delete(0,'end')
    heighttextfield.delete(0,'end')
    weighttextfield.delete(0,'end')

frame=Frame(
    mainwindow,
        padx=10,
        pady=10
)
frame.pack(expand=True)

agelabel=Label(
    frame,
    text="ENTER AGE : ")
agelabel.grid(row=1,column=1)
agetextfield=Entry(frame,
                   )
agetextfield.grid(row=1,column=2,pady=5)

genderlabel=Label(frame,
                  text="SELECT GENDER : ")
genderlabel.grid(row=2,column=1)

frame2=Frame(frame)
frame2.grid(row=2,column=2,pady=5)


maleradio=Radiobutton(
    frame2,
    text='MALE',
    variable=IntVar,   
    value=1
                      )
maleradio.pack(side=LEFT)
femaleradio=Radiobutton(
    frame2,
    text='FEMALE',
    variable=IntVar,
    value=2
                      )
femaleradio.pack(side=RIGHT)

heightlabel=Label(
    frame,
    text="ENTER YOUR HEIGHT (cm) : ",
)
heightlabel.grid(row=3,column=1)
heighttextfield=Entry(frame,)
heighttextfield.grid(row=3, column=2,pady=5)
weightlabel=Label(
    frame,
    text="ENTER YOUR WEIGHT (kg) : ",
)
weightlabel.grid(row=4,column=1)
weighttextfield=Entry(frame,)
weighttextfield.grid(row=4,column=2,pady=5)

frame3=Frame(frame)
frame3.grid(row=5,columnspan=3,pady=10)

calculate=Button(
    frame3,
    text='CALCULATE',
    command=calbmi,
)
calculate.pack(side=LEFT)

reset = Button(
    frame3,
    text='RESET',
    command=resetfun,
)
reset.pack(side=LEFT)

exit = Button(
    frame3,
    text='EXIT',
    command=lambda:mainwindow.destroy()
    
)
exit.pack(side=RIGHT)


mainwindow.mainloop()