##### GPA Calculator         Dalton Knapp

from tkinter import *
from tkinter.messagebox import showinfo

def GPA():
    pass #write a function to compute GPA

class GPACalculator(Frame):


    def __init__(self,parent=None):
        lst = []

        Frame.__init__(self,parent)
        grade1 = LabelFrame(self,text='Grade - %',padx=5,pady=5)
        grade1.pack(padx=10,pady=5)
        g1 = Entry(grade1)
        g1.pack()
        grade2 = LabelFrame(self,text='Grade - %',padx=5,pady=5)
        grade2.pack(padx=10,pady=5)
        g2 = Entry(grade2)
        g2.pack()
        grade3 = LabelFrame(self,text='Grade - %',padx=5,pady=5)
        grade3.pack(padx=10,pady=5)
        g3 = Entry(grade3)
        g3.pack()
        grade4 = LabelFrame(self,text='Grade - %',padx=5,pady=5)
        grade4.pack(padx=10,pady=5)
        g4 = Entry(grade4)
        g4.pack()
        def cmd():
            showinfo('GPA', message = 'This term\'s GPA: '+\
                     str(((float(g1.get())+float(g2.get())+\
                           float(g3.get())+float(g4.get()))/4)))
        b = Button(self,text='Compute',command=cmd,width=7,height=1)
        b.pack()

GPACalculator().pack()
