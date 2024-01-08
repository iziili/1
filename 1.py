from tkinter import *

def show_full():
        full_name = f"{ent_first_name.get()} {ent_last_name.get()}"
        lbl_full_name.config(text ="Hello " + full_name,fg="green")





window = Tk()
window.title("info")
window.resizable(0,0)
window.geometry("350x150")
window.config(bg = "lightblue")

lbl_first_name =Label(window,text = "first name: ",font= ("arial","12"),bg = "lightblue")
lbl_first_name.grid(row=0,column=1,padx=5,pady=5)
ent_first_name = Entry(window,width=20)
ent_first_name.grid(row=0,column= 2,padx=5,pady=10)

lbl_last_name =Label(window,text = "last name: ",font= ("arial","12"),bg = "lightblue")
lbl_last_name.grid(row=1,column=1,padx=10,pady=10)
ent_last_name = Entry(window,width=20)
ent_last_name.grid(row=1,column= 2,padx=10,pady=10)

btn_submit=Button(window,text = "submit",font=("arial","12"),command=show_full)
btn_submit.grid(row=3,column=2)

lbl_full_name=Label(window,text = "Hello",font=("arial","12"),bg = "lightblue")
lbl_full_name.grid(row=3,column=1,padx=10,pady=10)


window.mainloop()