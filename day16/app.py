import tkinter as ttk
from tkinter import font

app = ttk.Tk()

app.title('Attendance System')
app.geometry('600x400')
font_=font.Font(size=20)

ttk.Label(
    app,
    text='Face Recognition based Attendance system'

).pack()

def register():
    app.destroy()
    import login_admin
    with open('opr','w') as f:
        f.write('register')
    import login_admin
    

def attendance(): 
    
    print('attendance')

def clear_data():
    app.destroy()
    with open('opr' , 'w') as f:
        f.write('clear')
    import login_admin

ttk.Button(
    app, text='Register',command=register,font=font_,
    height=3,width=15,background="#FCF3CF").pack()
ttk.Button(
    app, text='Attendance',command=attendance,font=font_,
    height=3,width=15,background='#F1C40F').pack()
ttk.Button(app, text='Clear Data',command=clear_data,font=font_,
    height=3,width=15,background='#D4AC0D').pack()

app.mainloop()