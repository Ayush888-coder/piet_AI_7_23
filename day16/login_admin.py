import tkinter as ttk
from tkinter import font
from tkinter import messagebox as mb
login_app=ttk.Tk()
login_app.title('Register')
login_app.geometry('600x400')
font_=font.Font(size=20)

ttk.Label(
    login_app,
    text='Enter your credentials',
    font=font_

).place(x=30,y=20)

uname =ttk.Variable(login_app)
pwd =ttk.Variable(login_app)


ttk.Label(login_app,text='Username',font=font_).place(x=100,y=80)
ttk.Entry(login_app,font=font_,textvariable=uname).place(x=250,y=80)

ttk.Label(login_app,text='Password',font=font_).place(x=100,y=130)
ttk.Entry(login_app,font=font_,show='#',textvariable=pwd).place(x=250,y=130)

def submit():
    op =''
    with open('opr','r') as f:
        op =f.read()
    print(op)
    if len(op) > 0:
        userid = uname.get()
        password= pwd.get()
        p= open('pwd').read()
        uname.set('')
        pwd.set('')
        if userid =='admin' and password == p:
            print('login succesful')
            mb.showinfo('Success','Login Successful')

            if op == 'register':
                from tkinter.simpledialog import askstring
                name = askstring('Name','For whom you want to register?')                
                import register_face as rf
                rf.register(name)
            elif op == 'clear':
                import clear_data


        else:
            print('login failed')
            mb.showerror('Error','Login Failed')



ttk.Button(
    login_app,text='Submit',font=font_,command=submit,
    height=2,width=10,bg='#58D68D',
).place(x=250,y=220)


def back():
    login_app.destroy()
    with open('opr','w') as f:
        op =f.write('')
    import app

ttk.Button(
    login_app,text='Back',font=font_,command=back,
    height=2,width=10,bg='#BFC9CA',
).place(x=250,y=300)

login_app.mainloop()