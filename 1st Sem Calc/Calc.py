import customtkinter as ctk
from tkinter import *
ctk.set_appearance_mode("Dark")


def Basic_calculator():
    root = ctk.CTk()
    calc_root = ctk.CTkToplevel(root)


    calc_root.title("Simple calculator")
    calc_root.geometry("280x340")
    number_enter = ctk.CTkEntry(calc_root, width=280, height=100)
    number_enter.pack()

    def add_number(number):
        current = number_enter.get()
        number_enter.delete(0, END)
        number_enter.insert(0, current + str(number))
    def button_clear():
        number_enter.delete(0, END)
    def button_equal():
        second_number = int(number_enter.get())
        number_enter.delete(0, END)
        ans = f_num + second_number
        number_enter.insert(0, ans)
    def button_add():
        global first_number
        first_number = int(number_enter.get())
        global f_num
        f_num = first_number
        number_enter.delete(0, END)

    """____The frames of the rows___"""
    row_1 = ctk.CTkFrame(calc_root)
    row_2 = ctk.CTkFrame(calc_root)
    row_3 = ctk.CTkFrame(calc_root)
    row_4 = ctk.CTkFrame(calc_root)
    row_5 = ctk.CTkFrame(calc_root)

    row_1.pack()
    row_2.pack()
    row_3.pack()
    row_4.pack()
    row_5.pack()
    """___/The frames of the rows___"""

    btn_padx = 5
    btn_pady = 5
    btn_width = 60
    btn_heigh = 50
    opo_padx = 5
    opo_pady = 5
    opo_width = 60
    opo_hieght = 50
    # This os the button list; declaring the function for our window
    button_1 = ctk.CTkButton(row_3, text=1, width=btn_width, height=btn_heigh,  command=lambda: add_number(1))
    button_2 = ctk.CTkButton(row_3, text=2, width=btn_width, height=btn_heigh,  command=lambda: add_number(2))
    button_3 = ctk.CTkButton(row_3, text=3, width=btn_width, height=btn_heigh,  command=lambda: add_number(3))
    button_4 = ctk.CTkButton(row_2, text=4, width=btn_width, height=btn_heigh,  command=lambda: add_number(4))
    button_5 = ctk.CTkButton(row_2, text=5, width=btn_width, height=btn_heigh,  command=lambda: add_number(5))
    button_6 = ctk.CTkButton(row_2, text=6, width=btn_width, height=btn_heigh,  command=lambda: add_number(6))
    button_7 = ctk.CTkButton(row_1, text=7, width=btn_width, height=btn_heigh,  command=lambda: add_number(7))
    button_8 = ctk.CTkButton(row_1, text=8, width=btn_width, height=btn_heigh,  command=lambda: add_number(8))
    button_9 = ctk.CTkButton(row_1, text=9, width=btn_width, height=btn_heigh,   command=lambda: add_number(9))
    button_0 = ctk.CTkButton(row_4, text=0, width=btn_width, height=btn_heigh,  command=lambda: add_number(0))
    but_clear = ctk.CTkButton(row_4, text="Clear", width=opo_width, height=opo_hieght, command=button_clear)
    but_equal = ctk.CTkButton(row_4, text="=", width=opo_width, height=opo_hieght, command=button_equal)
    but_add = ctk.CTkButton(row_1, text="+", width=opo_width, height=opo_hieght, command=button_add)
    but_sub = ctk.CTkButton(row_2, text="-", width=opo_width, height=opo_hieght, )#command=button_sub)
    but_div = ctk.CTkButton(row_3, text="/", width=opo_width, height=opo_hieght, )#command=button_div)
    but_mul = ctk.CTkButton(row_4, text="*", width=opo_width, height=opo_hieght, )#command=button_mul)

    # Puting the buttons on the screen, as in  .

    button_1.pack(side=LEFT, padx=btn_padx, pady=btn_pady)
    button_2.pack(side=LEFT, padx=btn_padx, pady=btn_pady)
    button_3.pack(side=LEFT, padx=btn_padx, pady=btn_pady)

    button_4.pack(side=LEFT, padx=btn_padx, pady=btn_pady)
    button_5.pack(side=LEFT, padx=btn_padx, pady=btn_pady)
    button_6.pack(side=LEFT, padx=btn_padx, pady=btn_pady)

    button_7.pack(side=LEFT, padx=btn_padx, pady=btn_pady)
    button_8.pack(side=LEFT, padx=btn_padx, pady=btn_pady)
    button_9.pack(side=LEFT, padx=btn_padx, pady=btn_pady)

    button_0.pack(side=LEFT, padx=btn_padx, pady=btn_pady)
    but_clear.pack(side=LEFT, padx=5, pady=5)
    but_equal.pack(side=LEFT, padx=btn_padx, pady=btn_pady)
    but_add.pack(side=LEFT, padx=btn_padx, pady=btn_pady)
    but_sub.pack(side=LEFT, padx=btn_padx, pady=btn_pady)
    but_div.pack(side=LEFT, padx=btn_padx, pady=btn_pady)
    but_mul.pack(side=LEFT, padx=btn_padx, pady=btn_pady)



    calc_root.mainloop()



#Basic_calculator()