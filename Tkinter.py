from tkinter import *
from pymysql import *
from tkinter.font import BOLD,ITALIC
from tkinter import messagebox
from tkinter.ttk import  Treeview
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
        self.clear= Button(self, text="clear", font=('Arial', 20, BOLD),command=self.clear)
        self.clear.grid(row=9, column=5)

    def clear(self):
        self.a.delete(0,'end')
        self.b.delete(0,'end')
        self.c.delete(0, 'end')
        self.d.delete(0, 'end')
        self.e.delete(0, 'end')
        self.f.delete(0, 'end')
        self.g.delete(0, 'end')

    def erase(self):
        con.autocommit(True)
        qry="delete from jobs where number="+(self.n.get())
        ack=cur.execute(qry)
        if ack!=0:
            messagebox.showinfo("info","deleted")
    def ins(self):
        qry="""insert into jobs(regnum,picdate,customername,contact,issue,expected,amount)values('%s','%s','%s',%d,'%s',%d,%f)""" % \
            (self.a.get(),self.b.get(),self.c.get(),int(self.d.get()),self.e.get(),int(self.f.get()),float(self.g.get()))
        ack=cur.execute(qry)
        con.autocommit(True)
        if ack !=0:
            messagebox.showinfo("info","updated")
        else:messagebox.showinfo("info","not updated")
    def update(self):
        con.autocommit(True)
        qry="""update jobs set regnum='%s',picdate='%s',customername='%s',contact=%d,issue='%s',expected=%d,amount=%f where number=%d"""\
            %(self.a.get(),self.b.get(),self.c.get(),int(self.d.get()),self.e.get(),int(self.f.get()),float(self.g.get()),int(self.n.get()))
        ack=cur.execute(qry)
        if ack!=0:
            messagebox.showinfo("info","updates")
        else:
            messagebox.showinfo("info","not updated")
    def one(self):
        job=self.n.get()
        qry="select * from jobs where number="+job
        cur.execute(qry)
        single=cur.fetchone()
        self.a.insert(0,single[1])
        self.b.insert(0, single[2])
        self.c.insert(0, single[3])
        self.d.insert(0, single[4])
        self.e.insert(0, single[5])
        self.f.insert(0, single[6])
        self.g.insert(0, single[7])




    def vw(self):
        class Vw(Frame):
            def _init_(self,parent):
                Frame._init_(self,parent)
                self.CreateUI()
                self.LoadTable()
                self.grid(sticky=(N,S,E,W))
                parent.grid_rowconfigure(0,weight=1)
                parent.grid_columnconfigure(0, weight=1)
            def CreateUI(self):
                tv = Treeview(self)
                tv['columns']=('number','regnum','picdate','customername','contact','issue','expected','amount')
                tv.heading('#0',text='number',anchor='center')
                tv.column('#0',anchor='center')
                tv.heading('#1', text='regnum', anchor='center')
                tv.column('#1', anchor='center')
                tv.heading('#2', text='picdate', anchor='center')
                tv.column('#2', anchor='center')
                tv.heading('#3', text='customername', anchor='center')
                tv.column('#3', anchor='center')
                tv.heading('#4', text='contact', anchor='center')
                tv.column('#4', anchor='center')
                tv.heading('#5', text='issue', anchor='center')
                tv.column('#5', anchor='center')
                tv.heading('#6', text='expected', anchor='center')
                tv.column('#6', anchor='center')
                tv.heading('#7', text='amount', anchor='center')
                tv.column('#7', anchor='center')
                tv.grid(sticky=(N,W,E,S))
                self.treeview=tv
                self.grid_rowconfigure(0,weight=1)
                self.grid_columnconfigure(0,weight=1)
            def LoadTable(self):
                select="select * from jobs"
                cur.execute(select)
                result=cur.fetchall()
                for i in result:
                    self.treeview.insert("",'end',text=i[0],
                        values=(i[0],i[2],i[3],i[4],i[5],i[6],i[7]))
        root=Tk()
        root.title("every data")
        root.geometry("1080x700")
        Vw(root)


h=Home()
h.mainloop()