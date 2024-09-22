from tkinter import *
root = Tk()

# Top bar
top_frm = Frame(root, bg="blue")
top_frm.grid(row=0, columnspan=50, rowspan=20)

lable=Label(top_frm, text="Indomie", )
lable.pack()

mainloop()

