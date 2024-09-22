import customtkinter
from PIL import Image
import imaginary_app
import matrix_place


def imaginary():
    root.destroy()
    imaginary_app.imaginary_app()


def matrix():
    root.destroy()
    matrix_place.matrixes_app()


def home():

    global root
    root = customtkinter.CTk()
    root.geometry("960x525")

    """:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::CENTER WIDGETS"""
    """::::::::::CENTER IMG FRAME"""
    center_img_frm = customtkinter.CTkFrame(root, fg_color="#242424")
    center_img_frm.pack(fill="y", expand=True)
    """:::::::::::/CENTER IMAGE FRAME"""

    """##########CENTER IMAGE##########"""
    center_img = customtkinter.CTkImage(light_image=Image.open("einstein-removebg-preview.png"),
                                        dark_image=Image.open("einstein-removebg-preview.png"), size=(162, 162))
    customtkinter.CTkLabel(center_img_frm, image=center_img, text=None ).pack(side="bottom")
    """##########/CENTER IMAGE##########"""

    """:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::HORIZONTAL WIDGETS FRAME"""
    horizontal_img_frm = customtkinter.CTkFrame(root, fg_color="#242424")
    horizontal_img_frm.pack(fill="x")
    """::::::::::::::/HORIZONTAL WIDGETS FRAME"""

    """###############HORIZONTAL IMAGE#############"""
    horizontal_img0 = customtkinter.CTkImage(light_image=Image.open("scientit_pic_2-removebg-preview.png"),
                                            dark_image=Image.open("scientit_pic_2-removebg-preview.png"), size=(142, 142))
    horizontal_img1 = customtkinter.CTkImage(light_image=Image.open("yu-removebg-preview.png"),
                                            dark_image=Image.open("yu-removebg-preview.png"), size=(132, 132))
    """___________PADDING FRAME BOTTOM"""
    customtkinter.CTkFrame(root, fg_color="#242424", height=100, width=100).pack(fill="y", expand=True) # adds padding bottom
    """___________/PADDING FRAME BOTTOM"""

    # horizontal_img0 call in horizontal_img_frm
    customtkinter.CTkButton(horizontal_img_frm, image=horizontal_img0, text=None, fg_color="#242424", width=0,
                            hover_color="#2B2B2B").pack(side="left", padx=15)

    """___________PADDING FRAME in horizontal_img_frm 'left' """
    left_horizontal_frm = customtkinter.CTkFrame(horizontal_img_frm, height=102, fg_color="#242424")
    left_horizontal_frm.pack(side="left", expand=True, fill="x")
    customtkinter.CTkButton(left_horizontal_frm,command=matrix , fg_color="#242424", hover_color="#2B2B2B", text="Matrix\nCalculator", font=customtkinter.CTkFont(
        family="Courier", size=25,
    )).pack()
    """___________/PADDING FRAME in horizontal_img_frm 'left' """

    """___________PADDING FRAME in horizontal_img_frm 'middle' """
    middle_horizontal_frm = customtkinter.CTkFrame(horizontal_img_frm, height=102, width=202, fg_color="#242424")
    middle_horizontal_frm.pack(side="left")
    """___________/PADDING FRAME in horizontal_img_frm 'middle' """

    """___________PADDING FRAME in horizontal_img_frm 'right' """
    right_horizontal_frm = customtkinter.CTkFrame(horizontal_img_frm, height=102, fg_color="#242424")
    right_horizontal_frm.pack(side="left", expand=True, fill="x")
    customtkinter.CTkButton(right_horizontal_frm, command=imaginary, text="Imaginary\nCalculator", fg_color="#242424",
                            hover_color="#2B2B2B", font=customtkinter.CTkFont(size=25,
                                                                                                family="Courier")).pack()
    """___________/PADDING FRAME in horizontal_img_frm 'right' """

    # horizontal_img1 call in horizontal_img_frm
    customtkinter.CTkButton(horizontal_img_frm, image=horizontal_img1, width=0
                            , hover_color="#2B2B2B", text=None, fg_color="#242424",command=imaginary).pack(side="left", padx=12)
    """###############/HORIZONTAL IMAGE#############"""


    home = customtkinter.CTkImage(light_image=Image.open("Umatata-removebg-preview.png"),
                                  dark_image=Image.open("Umatata-removebg-preview.png"), size=(50,50))
    customtkinter.CTkLabel(root, image=home, text=None).place(x=10, y=10)

    root.mainloop()


home()