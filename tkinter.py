from tkinter import *
from pymysql import *
from tkinter.font import BOLD,ITALIC
from tkinter import messagebox
con=connect(host='localhost',database='kabilan',user='root',password='')
cur=con.cursor()
class Home(Tk):
    def _init_(self):
        Tk._init_(self)
        self.title("jobs")
        self.geometry("700x700")
        f=('Arial',15,ITALIC)
        self.head=Label(self,text="service",font=('Arial',20,BOLD) )
        self.head.grid(row=0,column=50)
        self.nlab = Label(self, text="job number", font=('Arial', 20, BOLD))
        self.nlab.grid(row=1, column=4)
        self.n = Entry(self, borderwidth='2')
        self.n.grid(row=1, column=40)
        self.alab = Label(self, text="vehicle registration number", font=('Arial', 20, BOLD))
        self.alab.grid(row=2, column=4)
        self.a = Entry(self, borderwidth='2')
        self.a.grid(row=2, column=40)
        self.blab = Label(self, text="date", font=('Arial', 20, BOLD))
        self.blab.grid(row=3, column=4)
        self.b = Entry(self, borderwidth='2')
        self.b.grid(row=3, column=40)
        self.clab = Label(self, text="ownername", font=('Arial', 20, BOLD))
        self.clab.grid(row=4, column=4)
        self.c = Entry(self, borderwidth='2')
        self.c.grid(row=4, column=40)
        self.dlab = Label(self, text="contact", font=('Arial', 20, BOLD))
        self.dlab.grid(row=5, column=4)
        self.d = Entry(self, borderwidth='2')
        self.d.grid(row=5, column=40)
        self.elab = Label(self, text="vehicle issue", font=('Arial', 20, BOLD))
        self.elab.grid(row=6, column=4)
        self.e = Entry(self, borderwidth='2')
        self.e.grid(row=6, column=40)
        self.flab = Label(self, text="delivery expercted date", font=('Arial', 20, BOLD))
        self.flab.grid(row=7, column=4)
        self.f = Entry(self, borderwidth='2')
        self.f.grid(row=7, column=40)
        self.glab = Label(self, text="amount", font=('Arial', 20, BOLD))
        self.glab.grid(row=8, column=4)
        self.g = Entry(self, borderwidth='2')
        self.g.grid(row=8, column=40)
        self.bu = Button(self, text="save", font=('Arial', 20, BOLD),command=self.ins)
        self.bu.grid(row=9, column=0)
        self.view= Button(self, text="view all", font=('Arial', 20, BOLD),command=self.vw)
        self.view.grid(row=9, column=1)
        self.vone = Button(self, text="view one", font=('Arial', 20, BOLD),command=self.one)
        self.vone.grid(row=9, column=2)
        self.edit = Button(self, text="update", font=('Arial', 20, BOLD),command=self.update)
        self.edit.grid(row=9, column=3)
        self.delete = Button(self, text="delete", font=('Arial', 20, BOLD),command=self.erase)
        self.delete.grid(row=9, column=4)
        self.clear= Button(self, text="clear", font=('Arial', 20, BOLD))
        self.clear.grid(row=9, column=5)



