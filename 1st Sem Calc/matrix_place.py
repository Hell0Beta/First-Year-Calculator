import customtkinter as ctk
from tkinter import *
#import Matrix_arithmetics as ma
import numpy as np


'''The function for the arithmetics'''
def matrix(x1, x2, x3, x4, x5, x6, x7, x8, x9):
    matrix_1 = np.array([[x1, x2, x3], [x4, x5, x6], [x7, x8, x9]])
    return matrix_1
def entry_enterer(z11, z12, z13, z21, z22, z23, z31, z32, z33):
    entered_entry = [z11, z12, z13, z21, z22, z23, z31, z32, z33]
    return entered_entry
def mat_sum():
    matrixa = matrix(int(x1.get()), int(x2.get()), int(x3.get()), int(x4.get()), int(x5.get()), int(x6.get()),
                     int(x7.get()), int(x8.get()), int(x9.get()))
    matrixb = matrix(int(y1.get()), int(y2.get()), int(y3.get()), int(y4.get()), int(y5.get()), int(y6.get()),
                     int(y7.get()), int(y8.get()), int(y9.get()))
    sum_matrix = matrixa + matrixb
    entries = z1, z2, z3, z4, z5, z6, z7, z8, z9
    count = 0
    for row in sum_matrix:
        for column in row:
            entries[count].delete(0, END)
            entries[count].insert(0, column)
            count += 1
def mat_sub():
    matrixa = matrix(int(x1.get()), int(x2.get()), int(x3.get()), int(x4.get()), int(x5.get()), int(x6.get()),
                     int(x7.get()), int(x8.get()), int(x9.get()))
    matrixb = matrix(int(y1.get()), int(y2.get()), int(y3.get()), int(y4.get()), int(y5.get()), int(y6.get()),
                     int(y7.get()), int(y8.get()), int(y9.get()))
    div_matrix = matrixa - matrixb
    entries = z1, z2, z3, z4, z5, z6, z7, z8, z9
    count = 0
    for row in div_matrix:
        for column in row:
            entries[count].delete(0, END)
            entries[count].insert(0, column)
            count += 1
def mat_multi():
    matrixa = matrix(int(x1.get()), int(x2.get()), int(x3.get()), int(x4.get()), int(x5.get()), int(x6.get()),
                     int(x7.get()), int(x8.get()), int(x9.get()))
    matrixb = matrix(int(y1.get()), int(y2.get()), int(y3.get()), int(y4.get()), int(y5.get()), int(y6.get()),
                     int(y7.get()), int(y8.get()), int(y9.get()))
    product_matrix = np.matmul(matrixa, matrixb)
    entries = z1, z2, z3, z4, z5, z6, z7, z8, z9
    count = 0
    for row in product_matrix:
        for column in row:
            entries[count].delete(0, END)
            entries[count].insert(0, column)
            count += 1
'''/The functions for the arithmetics'''

def matrixes_app():
    global info_frame
    global informed_frame
    global matrix1
    global matrix2
    global z1
    global z2
    global z3
    global z4
    global z5
    global z6
    global z7
    global z8
    global z9
    global x1
    global x2
    global x3
    global x4
    global x5
    global x6
    global x7
    global x8
    global x9
    global y1
    global y2
    global y3
    global y4
    global y5
    global y6
    global y7
    global y8
    global y9
    global root

    ctk.set_appearance_mode("Dark")
    root = ctk.CTk()
    root.geometry("903x525")

    """::::::::::::::::::::::::::::::::::::::TOP BAR::::::::::::::::::::::::::::::::::::::::"""
    """::::::::::::::::topbar_frm"""
    topbar_frm = ctk.CTkFrame(root, fg_color="#242424")
    topbar_frm.pack()
    """::::::::::::::::/topbar_frm"""

    topbar_text = ctk.CTkLabel(topbar_frm, text="Matrics__", font=ctk.CTkFont(family="Arial, Helvetica, sans-serif",
                                                                    size=35, weight="bold"))
    topbar_text.pack(side=LEFT, pady=15)


    """::::::::::::::::::::::::::/TOP BAR:::::::::::::::::::::::::::::::::"""

    """::::::::::::::::::::::::::SIDE BAR:::::::::::::::::::::::::::::::::::"""
    side_bar = ctk.CTkFrame(root, fg_color="#242424")
    side_bar.pack(side=LEFT)
    """-------root widgets_buttons--------"""
    sum_btn = ctk.CTkButton(side_bar, width=70, text="SUM", command=mat_sum)
    sum_btn.pack(pady=15, padx=20)

    diff_btn = ctk.CTkButton(side_bar, width=70, text="DIFF", command=mat_sub)
    diff_btn.pack(pady=15, padx=20)

    product_btn = ctk.CTkButton(side_bar, width=70, text="Product", command=mat_multi)
    product_btn.pack(pady=15, padx=20)

    """-------/root widgets_buttons--------"""
    """:::::::::::::::::::::::::/SIDE BAR:::::::::::::::::::::::::::::::::::::"""

    """:::::::::::::::::::::::::EQN ENTRY:::::::::::::::::::::::::::::::::::::"""

    """--------------minor entry frame--------"""
    minor_frm = ctk.CTkFrame(root, width=900 - 120, height=520 - 80)
    minor_frm.pack(expand=True, side=RIGHT, fill=BOTH)
    """-------------/minor entry frame--------"""

    """------Matrix entry frame---------"""
    input_frm = ctk.CTkFrame(minor_frm, width=100, height=100)
    frm_1 = ctk.CTkFrame(input_frm)
    frm_2 = ctk.CTkFrame(input_frm)
    def choice_box(option):
        combo = combobox.get()
        if combo == "Arithmetics":
            frm_1.grid(row=20, column=0, padx=20, pady=20)
            frm_2.grid(row=22, column=0, padx=20, pady=20)
        elif combo == "Inverse":
            frm_2.destroy()
            frm_2.pack_forget()
            frm_1.grid(row=20, column=0, padx=20, pady=20)

    combobox = ctk.CTkComboBox(minor_frm, values=["Choose an option", "Arithmetics", "Inverse"], command=choice_box)
    combobox.place(x=50, y=50)

    input_frm.pack(side=LEFT, padx=50, ipadx=20)
    label = ctk.CTkLabel(input_frm, text="Adding 3X3 Matrix")
    label.grid()


    """------\Matrix entry frame---------"""
    entry_width = 30
    entry_height = 30
    grid_padx = 10
    grid_pady = 8
    x1 = ctk.CTkEntry(frm_1, width=entry_width, height=entry_height)
    a = x1.get()
    print(a)
    x1.grid(row=0, column=0, padx=grid_padx, pady=grid_pady)

    x2 = ctk.CTkEntry(frm_1, width=entry_width, height=entry_height)
    x2.grid(row=0, column=1, padx=grid_padx, pady=grid_pady)

    x3 = ctk.CTkEntry(frm_1, width=entry_width, height=entry_height)
    x3.grid(row=0, column=2, padx=grid_padx, pady=grid_pady)

    x4 = ctk.CTkEntry(frm_1, width=entry_width, height=entry_height)
    x4.grid(row=1, column=0, padx=grid_padx, pady=grid_pady)

    x5 = ctk.CTkEntry(frm_1, width=entry_width, height=entry_height)
    x5.grid(row=1, column=1, padx=grid_padx, pady=grid_pady)

    x6 = ctk.CTkEntry(frm_1, width=entry_width, height=entry_height)
    x6.grid(row=1, column=2, padx=grid_padx, pady=grid_pady)

    x7 = ctk.CTkEntry(frm_1, width=entry_width, height=entry_height)
    x7.grid(row=2, column=0, padx=grid_padx, pady=grid_pady)

    x8 = ctk.CTkEntry(frm_1, width=entry_width, height=entry_height)
    x8.grid(row=2, column=1, padx=grid_padx, pady=grid_pady)

    x9 = ctk.CTkEntry(frm_1, width=entry_width, height=entry_height)
    x9.grid(row=2, column=2, padx=grid_padx, pady=grid_pady)

    # The operator between
    operator = ctk.CTkLabel(input_frm, text="+")
    operator.grid(row=21, column=0)

    # The second matrix value.
    y1 = ctk.CTkEntry(frm_2, width=entry_width, height=entry_height)
    y1.grid(row=0, column=0, padx=grid_padx, pady=grid_pady)

    y2 = ctk.CTkEntry(frm_2, width=entry_width, height=entry_height)
    y2.grid(row=0, column=1, padx=grid_padx, pady=grid_pady)

    y3 = ctk.CTkEntry(frm_2, width=entry_width, height=entry_height)
    y3.grid(row=0, column=2, padx=grid_padx, pady=grid_pady)

    y4 = ctk.CTkEntry(frm_2, width=entry_width, height=entry_height)
    y4.grid(row=1, column=0, padx=grid_padx, pady=grid_pady)

    y5 = ctk.CTkEntry(frm_2, width=entry_width, height=entry_height)
    y5.grid(row=1, column=1, padx=grid_padx, pady=grid_pady)

    y6 = ctk.CTkEntry(frm_2, width=entry_width, height=entry_height)
    y6.grid(row=1, column=2, padx=grid_padx, pady=grid_pady)

    y7 = ctk.CTkEntry(frm_2, width=entry_width, height=entry_height)
    y7.grid(row=2, column=0, padx=grid_padx, pady=grid_pady)

    y8 = ctk.CTkEntry(frm_2, width=entry_width, height=entry_height)
    y8.grid(row=2, column=1, padx=grid_padx, pady=grid_pady)

    y9 = ctk.CTkEntry(frm_2, width=entry_width, height=entry_height)
    y9.grid(row=2, column=2, padx=grid_padx, pady=grid_pady)

    matrix2 = matrix(y1.get(), y2.get(), y3.get(), y4.get(), y5.get(), y6.get(), y7.get(), y8.get(), y9.get())

    """-------eqn entry widgets_buttons--------"""

    """:::::::::::::widgets_frm"""
    widget_frm = ctk.CTkFrame(minor_frm, fg_color="#2B2B2B")
    widget_frm.pack(side=BOTTOM, pady=25)
    """:::::::::::::/widgets_frm"""

    euler_conv = ctk.CTkButton(widget_frm, width=70, text="Cofactors")
    euler_conv.pack(side=LEFT, padx=10)

    polar_conv = ctk.CTkButton(widget_frm, width=70, text="Transposition")
    polar_conv.pack(side=LEFT, padx=10)

    norm_conv = ctk.CTkButton(widget_frm, width=70, text="inverse")
    norm_conv.pack(side=LEFT, padx=10)

    norm_conv = ctk.CTkButton(widget_frm, width=70, text="Determinant")
    norm_conv.pack(side=LEFT, padx=10)
    """-------/eqn entry widgets_buttons--------"""

    """::::::::::::::::::::::::/EQN ENTRY:::::::::::::::::::::::::::::::::::::"""

    """::::::::::::::::::::::::INFO FRAME:::::::::::::::::::::::::::::::::::::"""
    info_frame = ctk.CTkScrollableFrame(minor_frm, width=300, height=300)
    info_frame.pack(expand=True, fill=BOTH, padx=15, pady=25)
    frm_3 = ctk.CTkFrame(info_frame)
    frm_3.pack(side=LEFT, padx=25)

    matrixinfo = ctk.CTkTextbox(info_frame, width=500)
    matrixinfo.pack(side=LEFT, padx=25, expand=True, fill=X)
    matrixinfo.insert("0.0", "Video provides a powerful way to help you prove your point. "
                             "When you click Online Video, "
                             "you can paste in the embed code for the video you want to add."
                             "You can also type a keyword to search online for the video that best fits your document. "
                             "To make your document look professionally produced, "
                             "Word provides header, footer, cover page,"
                             "and text box designs that complement each other. For example, "
                             "you can add a matching cover page, header, and sidebar.")

    operationwork = ctk.CTkTextbox(info_frame)
    operationwork.pack(side=LEFT, padx=25, expand=True, fill=X)
    operationwork.insert("0.0", "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.")

    # Solution
    z1 = ctk.CTkEntry(frm_3, width=entry_width, height=entry_height)
    z1.grid(row=0, column=0, padx=grid_padx, pady=grid_pady)

    z2 = ctk.CTkEntry(frm_3, width=entry_width, height=entry_height)
    z2.grid(row=0, column=1,  padx=grid_padx, pady=grid_pady)

    z3 = ctk.CTkEntry(frm_3, width=entry_width, height=entry_height)
    z3.grid(row=0, column=2,  padx=grid_padx, pady=grid_pady)

    z4 = ctk.CTkEntry(frm_3, width=entry_width, height=entry_height)
    z4.grid(row=1, column=0,  padx=grid_padx, pady=grid_pady)

    z5 = ctk.CTkEntry(frm_3, width=entry_width, height=entry_height)
    z5.grid(row=1, column=1,  padx=grid_padx, pady=grid_pady)

    z6 = ctk.CTkEntry(frm_3, width=entry_width, height=entry_height)
    z6.grid(row=1, column=2,  padx=grid_padx, pady=grid_pady)

    z7 = ctk.CTkEntry(frm_3, width=entry_width, height=entry_height)
    z7.grid(row=2, column=0,  padx=grid_padx, pady=grid_pady)

    z8 = ctk.CTkEntry(frm_3, width=entry_width, height=entry_height)
    z8.grid(row=2, column=1,  padx=grid_padx, pady=grid_pady)

    z9 = ctk.CTkEntry(frm_3, width=entry_width, height=entry_height)
    z9.grid(row=2, column=2,  padx=grid_padx, pady=grid_pady)

    informed_frame = ctk.CTkFrame(info_frame, fg_color="#333333")
    informed_frame.pack()
    """::::::::::::::::::::::::/INFO FRAME:::::::::::::::::::::::::::::::::::::"""
    root.mainloop()




#matrixes_app()



