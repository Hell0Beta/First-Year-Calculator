import customtkinter
import imaginary as im
from tkinter import *
from PIL import Image
import graphed as gr
from random import choice
import math
import home
import Calc

customtkinter.set_appearance_mode("Dark")

px = []
py = []
au = 0
bi = 12
#
#def on_enter(event):
#    global img0
#    global img1
#    global img2
#    global img3
#
#
#    print("32")
#
#
#def on_leave(event):
#    info_text_frm.configure(graph_btn, image=img0)
#

def calc():
    Calc.Basic_calculator()


def homey():
    root.destroy()
    home.home()


def active_btn():
    active = True
    return active


def equation_one():
    global eqn1
    global eqn1_a
    global eqn1_b

    eqn1 = equation_1.get()
    equated1.delete(0.0, END)
    equated1.insert(0.0, f"○ {eqn1}")
    equated1.grid(row=0, column=0, padx=5, pady=5)

    eqn1_a = int(im.checker_r(eqn1))
    eqn1_b = int(im.checker_i(eqn1))

    px.append(eqn1_a)
    py.append(eqn1_b)

    return eqn1


def equation_two():
    global eqn2
    global eqn2_a
    global eqn2_b
    eqn2 = equation_2.get()


    equated2.delete(0.0, END)
    equated2.insert(0.0, f"○ {eqn2}")
    equated2.grid(row=0, column=1, padx=5, pady=5)

    eqn2_a = int(im.checker_r(eqn2))
    eqn2_b = int(im.checker_i(eqn2))

    px.append(eqn2_a)
    py.append(eqn2_b)

    return eqn2


def imaginary_sum():
    global pic
    global txt
    real1 = im.checker_r(eqn1)
    im1 = im.checker_i(eqn1)
    real2 = im.checker_r(eqn2)
    im2 = im.checker_i(eqn2)

    imaginarysum = f"SUM: \n○ {real1 + real2}+({im1 + im2})i"
    imaginarytextbox.pack()
    imaginarytextbox.delete(0.0, END)
    imaginarytextbox.insert(0.0, imaginarysum)

    eqnr_a = int(real1+real2)
    eqnr_b = int(im1+im2)


    infotext= "• The sum of an imaginary " \
                  "number is calculated by adding \n" \
                  "real parts and imaginary" \
              "parts of an imaginary number" \
                  f"\n\nSUM: {real1} + {real2} + ({im1} + {im2})i"
    txt.delete(0.0, END)
    txt.insert(0.0, infotext)

    px.clear()
    py.clear()

    px.append(eqn1_a)
    py.append(eqn1_b)
    px.append(eqn2_a)
    py.append(eqn2_b)
    px.append(eqnr_a)
    py.append(eqnr_b)

    graph_btn.pack(padx=au, pady=bi)


def imaginary_diff():
    global img
    real1 = im.checker_r(eqn1)
    im1 = im.checker_i(eqn1)
    real2 = im.checker_r(eqn2)
    im2 = im.checker_i(eqn2)

    imaginarydiff = f"Difference: \n{real1 - real2}+({im1 - im2})i"

    imaginarytextbox.pack()
    imaginarytextbox.delete(0.0, END)
    imaginarytextbox.insert(0.0, imaginarydiff)
    graph_btn.pack(padx=au, pady=bi)

    eqnr_a = int(real1 + real2)
    eqnr_b = int(im1 + im1)

    infotext = "• The difference of an imaginary number is " \
               "calculated by subtracting the real parts and " \
               "imaginary parts of an imaginary number " \
               f"\n\nDiff: {real1} - {real2} + ({im1} - {im2})i"
    txt.delete(0.0, END)
    txt.insert(0.0, infotext)


    px.clear()
    py.clear()

    px.append(eqnr_a)
    py.append(eqnr_b)
    px.append(eqn1_a)
    py.append(eqn1_b)
    px.append(eqn2_a)
    py.append(eqn2_b)


def imaginary_product():
    imaginaryproduct = im.ima_product(eqn1, eqn2)
    imaginarytextbox.pack()
    imaginarytextbox.delete(0.0, END)
    imaginarytextbox.insert(0.0, imaginaryproduct)
    graph_btn.pack(padx=au, pady=bi)

    a = im.checker_r(eqn1)
    b = im.checker_i(eqn1)
    c = im.checker_r(eqn2)
    d = im.checker_i(eqn2)

    eqnr_a = int(a * c - (b * d))
    eqnr_b = int(a * c + (a * d))

    infotext = "• The product of an imaginary number is " \
               "described as 'The difference between " \
               "the product of the real and imaginary parts" \
               "summed with imaginary sum of the product of " \
               "the real and alternate value of the imaginary" \
                "\n\nProduct: real1 * real2 - (imaginary1 * imaginary2)  +  (real1 * real2 + (real1 * imaginary2))i"

    txt.delete(0.0, END)
    txt.insert(0.0, infotext)

    px.clear()
    py.clear()

    px.append(eqnr_a)
    py.append(eqnr_b)
    px.append(eqn1_a)
    py.append(eqn1_b)
    px.append(eqn2_a)
    py.append(eqn2_b)


def imaginary_quotient():
    imaginaryquotient = f"Quotient: \n○{im.ima_quotient(eqn1, eqn2)}"
    imaginarytextbox.pack()
    imaginarytextbox.delete(0.0, END)
    imaginarytextbox.insert(0.0, imaginaryquotient)
    graph_btn.pack(padx=au, pady=bi)

    a = im.checker_r(eqn1)
    b = im.checker_i(eqn1)
    c = im.checker_r(eqn2)
    d = im.checker_i(eqn2)

    eqnr_a = round((a * c + b * d) / ((c ** 2) + (d ** 2)), 3)
    eqnr_b = round((a * d + b * c) / ((c ** 2) + (d ** 2)), 3)

    infotext = "• The quotient between imaginary numbers is " \
               "described as 'The product of one number by " \
               "the conjugate of the other divided by the" \
               " squared sum of their imaginary parts" \
               "\n\nQuotient: (a * c + b * d) / ((c ** 2) + (d ** 2))  +  (a * d + b * c) / ((c ** 2) + (d ** 2))i"

    txt.delete(0.0, END)
    txt.insert(0.0, infotext)

    px.clear()
    py.clear()

    px.append(eqnr_a)
    py.append(eqnr_b)
    px.append(eqn1_a)
    py.append(eqn1_b)
    px.append(eqn2_a)
    py.append(eqn2_b)


def conv_euler():
    try:
        real = im.checker_r(eqn1)
        ima = im.checker_i(eqn1)
        converted_euler1 = im.converter_euler(im=ima, real=real)

        equation_1.delete(0, 100)
        equation_1.insert(0, converted_euler1)
    except ValueError:
        pass

    try:
        real2 = im.checker_r(eqn2)
        ima2 = im.checker_i(eqn2)
        converted_euler2 = im.converter_euler(im=ima2, real=real2)
        equation_2.delete(0, 100)
        equation_2.insert(0, converted_euler2)
    except ValueError:
        pass


def conv_polar():
    real1 = im.checker_r(eqn1)
    im1 = im.checker_i(eqn1)
    real2 = im.checker_r(eqn2)
    im2 = im.checker_i(eqn2)

    result = im.converter_polar(real1, im1)
    result2 = im.converter_polar(real2, im2)

    equation_1.delete(0, 100)
    equation_2.delete(0, 100)

    equation_1.insert(0, result)
    equation_2.insert(0, result2)


def conv_imagine():
    eqned = equation_1.get()
    eqned2 = equation_2.get()
    r = im.polar_checker_mod(eqned)
    arg = im.polar_checker_arg(eqned)
    r1 = im.polar_checker_mod(eqned2)
    arg1 = im.polar_checker_arg(eqned2)
    a = r*math.cos(arg)
    b = r*math.sin(arg)
    c = r1*math.cos(arg1)
    d = r1*math.sin(arg1)

    result = f"{round(a, 2)}+({round(b, 2)})i"
    result1 = f"{round(c, 2)}+{round(d, 2)}i"

    equation_1.delete(0, 100)
    equation_2.delete(0, 100)

    equation_1.insert(0, result)
    equation_2.insert(0, result1)


def imaginary_app():
    global equation_1
    global info_frame
    global equation_2
    global graph_btn
    global equated1
    global equated2
    global imaginarytextbox
    global imaginarytextbox
    global info_text_frm
    global txt
    global img0
    global img1
    global img2
    global img3
    global graph_btn
    global root

    root = customtkinter.CTk()
    root.geometry("960x525")

    """::::::::::::::::::::::::::::::::::::::TOP BAR::::::::::::::::::::::::::::::::::::::::"""
    """::::::::::::::::topbar_frm"""
    mega_top_frm = customtkinter.CTkFrame(root, fg_color="#242424", )
    mega_top_frm.pack()

    topbar_frm = customtkinter.CTkFrame(mega_top_frm, fg_color="#242424", )
    topbar_frm.grid(row=0, column=1)
    side_btn_frm = customtkinter.CTkFrame(mega_top_frm, fg_color="#242424", )
    side_btn_frm.grid(row=0, column=2)
    frm_home = customtkinter.CTkFrame(root)
    frm_home.place(x=10, y=8)
    """::::::::::::::::/topbar_frm"""

    topbar_text = customtkinter.CTkLabel(topbar_frm,
                                         text="imaginary_numbers",
                                         font=customtkinter.CTkFont(family="Arial, Helvetica, sans-serif", size=35,
                                                                    weight="bold"))
    topbar_text.pack(pady=15)
    img = customtkinter.CTkImage(light_image=Image.open("einstein-removebg-preview.png"),
                                 dark_image=Image.open("einstein-removebg-preview.png"), size=(55, 55))

    d = customtkinter.CTkButton(side_btn_frm, text=None, width=1, fg_color="#242424", image=img)

    d.pack(pady=15, side=RIGHT)

    img4btn = customtkinter.CTkImage(light_image=Image.open("Umatata-removebg-preview.png"),
                                     dark_image=Image.open("Umatata-removebg-preview.png"), size=(65, 65))

    home_btn = customtkinter.CTkButton(frm_home, text=None, image=img4btn, width=10, fg_color="#242424",
                                       bg_color="#242424", hover_color="#535252", command=homey)
    home_btn.pack(side=LEFT)

    """::::::::::::::::::::::::::/TOP BAR:::::::::::::::::::::::::::::::::"""

    """::::::::::::::::::::::::::SIDE BAR:::::::::::::::::::::::::::::::::::"""
    side_bar = customtkinter.CTkFrame(root, fg_color="#242424")
    side_bar.pack(side=LEFT, fill=Y, pady=12)
    """-------root widgets_buttons--------"""
    sum_btn = customtkinter.CTkButton(side_bar, width=70, text="SUM", command=imaginary_sum)
    sum_btn.pack(pady=25, padx=20)

    diff_btn = customtkinter.CTkButton(side_bar, width=70, text="DIFF", command=imaginary_diff)
    diff_btn.pack(pady=15, padx=20)

    product_btn = customtkinter.CTkButton(side_bar, width=70, text="Product", command=imaginary_product)
    product_btn.pack(pady=15, padx=20)

    div_btn = customtkinter.CTkButton(side_bar, width=70, text="Division", command=imaginary_quotient)
    div_btn.pack(pady=20, padx=20)

    img4calcbtn = customtkinter.CTkImage(light_image=Image.open("Calc_button_0-removebg-preview.png"),
                                         dark_image=Image.open("Calc_button_0-removebg-preview.png"), size=(75, 75))
    calc_btn = customtkinter.CTkButton(side_bar, image=img4calcbtn, text=None, fg_color="#242424",
                                       bg_color="#242424", width=10, command=calc)
    calc_btn.pack(side=BOTTOM, anchor=S)
    """-------/root widgets_buttons--------"""
    """:::::::::::::::::::::::::/SIDE BAR:::::::::::::::::::::::::::::::::::::"""

    """:::::::::::::::::::::::::EQN ENTRY:::::::::::::::::::::::::::::::::::::"""
    """--------------eqn entry frame--------"""
    eqn_entry_frame = customtkinter.CTkFrame(root, width=900 - 120, height=520 - 80, )
    eqn_entry_frame.pack(expand=True, side=RIGHT, fill=BOTH)
    """-------------/eqn entry frame--------"""

    """-------eqn entry widgets_entry--------"""
    eqn_frame = customtkinter.CTkFrame(eqn_entry_frame, fg_color="#2B2B2B")
    eqn_frame.pack(side=LEFT, padx=12, anchor=NW, pady=40)

    """:::::::::::eqn1_frm"""
    eqn1_frm = customtkinter.CTkFrame(eqn_frame)
    eqn1_frm.pack(pady=55, expand=True, fill=X)
    """:::::::::::/eqn1_frm"""

    equation_1 = customtkinter.CTkEntry(eqn1_frm, width=200)
    equation_1.pack(expand=True, fill=X)

    eqn1_btn = customtkinter.CTkButton(eqn1_frm, text="Equation 1", width=80, command=equation_one)
    eqn1_btn.pack(expand=True, fill=X, padx=90, pady=8)

    """::::::::::::eqn2_frm"""
    eqn2_frm = customtkinter.CTkFrame(eqn_frame)
    eqn2_frm.pack(expand=True, fill=X)
    """:::::::::::::/eqn2_frm"""

    equation_2 = customtkinter.CTkEntry(eqn2_frm, width=200)
    equation_2.pack(expand=True, fill=X)

    eqn2_btn = customtkinter.CTkButton(eqn2_frm, text="Equation 2", width=80, command=equation_two)
    eqn2_btn.pack(expand=True, fill=X, padx=90, pady=8)

    """-------eqn entry widgets_buttons--------"""

    """:::::::::::::widgets_frm"""
    widget_frm = customtkinter.CTkFrame(eqn_entry_frame, fg_color="#2B2B2B")
    widget_frm.pack(side=BOTTOM, pady=25)
    """:::::::::::::/widgets_frm"""

    euler_conv = customtkinter.CTkButton(widget_frm, width=70, text="Euler's Form", command=conv_euler, )
    euler_conv.pack(side=LEFT, padx=10)

    polar_conv = customtkinter.CTkButton(widget_frm, width=70, text="Polar Form", command=conv_polar)
    polar_conv.pack(side=LEFT, padx=10)

    norm_conv = customtkinter.CTkButton(widget_frm, width=70, text="z=a+bi", command=conv_imagine)
    norm_conv.pack(padx=10)

    """-------/eqn entry widgets_buttons--------"""

    """::::::::::::::::::::::::/EQN ENTRY:::::::::::::::::::::::::::::::::::::"""

    """::::::::::::::::::::::::INFO FRAME:::::::::::::::::::::::::::::::::::::"""
    info_frame = customtkinter.CTkScrollableFrame(eqn_entry_frame)
    info_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

    informed_frm = customtkinter.CTkFrame(info_frame, fg_color="#333333", )
    informed_frm.pack(pady=12)

    equated1 = customtkinter.CTkTextbox(informed_frm, bg_color="#333333", width=100,
                                        height=10,font=customtkinter.CTkFont(size=15))
    equated2 = customtkinter.CTkTextbox(informed_frm, bg_color="#333333", width=100,
                                        height=10, font=customtkinter.CTkFont(size=15))

    imaginarytextbox = customtkinter.CTkTextbox(info_frame, width=120, height=50, font=customtkinter.CTkFont(size=15))

    img0 = customtkinter.CTkImage(light_image=Image.open("OIG1.snuDqLpujs7.jgyo-removebg-preview (1).png"),
                                 dark_image=Image.open("OIG1.snuDqLpujs7.jgyo-removebg-preview (1).png"), size=(185, 185))
    img1 = customtkinter.CTkImage(light_image=Image.open("yu-removebg-preview.png"),
                                  dark_image=Image.open("yu-removebg-preview.png"), size=(185, 185))
    img2 = customtkinter.CTkImage(light_image=Image.open("einstein-removebg-preview.png"),
                                  dark_image=Image.open("einstein-removebg-preview.png"), size=(185, 185))
    img3 = customtkinter.CTkImage(light_image=Image.open("scientit_pic_2-removebg-preview.png"),
                                  dark_image=Image.open("scientit_pic_2-removebg-preview.png"), size=(185, 185))

    img_lst = [img0, img1, img2, img3]
    info_text_frm = customtkinter.CTkFrame(info_frame, fg_color="#333333")
    info_text_frm.pack(fill=BOTH)

    graph_btn = customtkinter.CTkButton(info_text_frm, text=None, image=choice(img_lst), fg_color="#333333", width=5,
                                        command=lambda:gr.fun(px, py), hover_color="#2B2B2B")

    txt = customtkinter.CTkTextbox(info_text_frm, fg_color="#333333")
    txt.pack(side=LEFT, fill=BOTH, expand=True, pady=12)
# 
# graph_btn.bind('<Enter>', on_enter, add='+')
# # you may also want to bind to '<Leave>' to complete the hover handler
# graph_btn.bind("<Leave>", on_leave, add='+')


    """::::::::::::::::::::::::/INFO FRAME:::::::::::::::::::::::::::::::::::::"""
    root.mainloop()


#imaginary_app()



